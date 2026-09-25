# Group Worksheet: Meaning of the Incompressible Navier-Stokes Terms

## Context
You have 40 minutes in your group room.

Focus today:
- Physical meaning of the terms in the incompressible Navier-Stokes equations
- Which terms dominate in different flow situations
- How dimensionless groups support your physical interpretation

Not part of this worksheet:
- Couette flow
- Full analytical solutions to Navier-Stokes

Equations used:

$$
\rho\left(\frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V}\cdot\nabla)\mathbf{V}\right)
= -\nabla p + \mu\nabla^2\mathbf{V} + \rho\mathbf{g}
$$

$$
\nabla\cdot\mathbf{V}=0
$$

## Group Setup
- Group size: 3 to 5 students
- Roles: facilitator, recorder, presenter, checker
- Deliverables: one shared answer sheet per group

## Time Plan
1. Exercise 1: 12 min
2. Exercise 2: 13 min
3. Exercise 3: 15 min

Total: 40 min

---

## Exercise 1 (12 min): Translate Equation to Physics

For each term below, fill out the table.

Terms:
- $\rho \frac{\partial \mathbf{V}}{\partial t}$
- $\rho(\mathbf{V}\cdot\nabla)\mathbf{V}$
- $-\nabla p$
- $\mu\nabla^2\mathbf{V}$
- $\rho\mathbf{g}$
- $\nabla\cdot\mathbf{V}=0$

For each term, write:
1. Plain-language meaning (one sentence)
2. Main cause
3. Main effect on flow
4. Unit consistency check (for momentum equation terms: N/m^3)

Template:

| Term | Meaning in words | Main cause | Main effect | Units check |
|---|---|---|---|---|
| Example: $-\nabla p$ | Pressure changes in space drive fluid from high to low pressure | Pressure differences | Acceleration/deceleration | Pa/m = N/m^3 |

Deliverable:
- Completed table for all terms

---

## Exercise 2 (13 min): Which Terms Dominate?

For each scenario:
1. Rank terms from most important to least important
2. State likely dominant balance
3. Give 2 to 3 bullets explaining your choice using flow scales

Useful scaling estimates:
- Unsteady inertia: $\rho U/T$
- Convective inertia: $\rho U^2/L$
- Pressure gradient: $\Delta p/L$
- Viscous term: $\mu U/L^2$
- Gravity: $\rho g$

### Scenario A
A pump is switched off in a long pipeline. Flow rate decays over time.

### Scenario B
High-speed water passes through a sharp 90 degree pipe bend.

### Scenario C
Water is nearly at rest in a tall vertical tank.

Deliverable:
- Ranking + dominant balance + short justification for A, B, C

---

## Exercise 3 (15 min): Mini Non-Dimensionalization and Regime Map

Use characteristic scales $U$, $L$, $T$, $\Delta p$ and identify:
- Reynolds number: $Re = \frac{\rho U L}{\mu}$
- Strouhal number: $St = \frac{L}{U T}$
- Froude number: $Fr = \frac{U}{\sqrt{gL}}$
- Euler number: $Eu = \frac{\Delta p}{\rho U^2}$

Tasks:
1. Explain what high vs low values of each group mean physically
2. Draw a simple regime map with axes $Re$ and $Fr$
3. Place Scenario A, B, C on your map
4. For each point, state one likely dominant term balance

Deliverable:
- One regime map and one-line interpretation for each scenario

---

## Final 2-Minute Wrap-Up
Be ready to present:
- One surprising insight from your group
- One term that was hardest to interpret physically
- One scenario where your term ranking was uncertain
