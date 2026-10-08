# Note to self:

### Run local webserver

``bash
python3 -m http.server
``

### Browse local webserver

[localhost:8000/](http://localhost:8000/)

### Regenerate slide-deck PDFs

The "PDF" links on the index page point to static files, matching what each
deck looks like when presented (16:9, all fragments revealed). Regenerate them
after editing any slides:

``bash
pip install -r requirements.txt   # first time only
python3 generate_pdf.py
python3 generate_index.py
``
