#!/usr/bin/env python3
"""Export each reveal.js slide deck in this repo to a static PDF.

Like generate_index.py, this scans the repo for slide decks and writes an
output file next to the source (here, <deck>.pdf next to <deck>.html). Run it
whenever slides change so the "PDF" links on the index page stay up to date:

    python3 generate_pdf.py                       # every deck
    python3 generate_pdf.py fluid-mechanics        # only decks in one folder

Requires the "playwright" package (pip install playwright) and a local Chrome
install. Does not need `playwright install`, since it drives the existing
Chrome via its executable path instead of downloading a bundled browser.
"""

import os
import sys
import threading
import time
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from playwright.sync_api import sync_playwright

# Base directory and folders to ignore, matching generate_index.py
base_dir = "."
ignore_folders = ["reveal.js", "__pycache__", "tools", "node_modules", ".git"]

CHROME_CANDIDATES = [
    os.environ.get("CHROME_PATH"),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/usr/bin/chromium",
]


def find_chrome():
    for candidate in CHROME_CANDIDATES:
        if candidate and os.path.exists(candidate):
            return candidate
    raise SystemExit(
        "Could not find a local Chrome/Chromium install. Set the CHROME_PATH "
        "environment variable to your browser executable and try again."
    )


def find_decks(only_folders):
    decks = []
    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if folder in ignore_folders or not os.path.isdir(folder_path):
            continue
        if only_folders and folder not in only_folders:
            continue

        for file in sorted(os.listdir(folder_path)):
            if file.endswith(".html"):
                decks.append(os.path.join(folder, file))
    return decks


class QuietRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # keep script output focused on export progress


def start_static_server():
    server = ThreadingHTTPServer(("127.0.0.1", 0), QuietRequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def export_deck_to_pdf(browser, base_url, deck_relative_path):
    out_path = deck_relative_path[:-5] + ".pdf"
    url = f"{base_url}/{deck_relative_path}?print-pdf"

    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    try:
        page.goto(url, wait_until="load", timeout=60000)

        # Wait for Reveal's print view to finish building its paginated DOM
        # (one .pdf-page per slide) instead of guessing with a fixed delay.
        page.wait_for_function(
            "document.querySelectorAll('.pdf-page').length > 0", timeout=30000
        )

        # Let webfonts, KaTeX and images finish painting.
        page.evaluate("document.fonts ? document.fonts.ready : null")
        page.wait_for_timeout(500)

        page.pdf(path=out_path, print_background=True, prefer_css_page_size=True)
        return out_path
    finally:
        page.close()


def main():
    only_folders = sys.argv[1:]
    decks = find_decks(only_folders)

    if not decks:
        print("No slide decks found.")
        return

    chrome_path = find_chrome()
    server = start_static_server()
    base_url = f"http://127.0.0.1:{server.server_address[1]}"

    exported = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome_path, headless=True)
        try:
            for deck in decks:
                print(f"Exporting {deck} ... ", end="", flush=True)
                try:
                    out_path = export_deck_to_pdf(browser, base_url, deck)
                    print(f"done -> {out_path}")
                    exported += 1
                except Exception as err:
                    print("FAILED")
                    print(f"  {err}")
        finally:
            browser.close()

    server.shutdown()
    print(f"Generated {exported} of {len(decks)} slide deck PDFs.")


if __name__ == "__main__":
    main()
