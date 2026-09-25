# Teacher Key: Group Worksheet on Incompressible Navier-Stokes Terms

## Intended Outcomes
By the end of the 40-minute session, students should be able to:
- Explain each NSE term in physical language
- Identify likely dominant balances in practical scenarios
- Use dimensionless groups to support qualitative reasoning

## Timing and Facilitation
1. Exercise 1 (12 min): circulate and check for term-level misconceptions
2. Exercise 2 (13 min): push students to justify rankings using scaling, not intuition only
3. Exercise 3 (15 min): ensure students connect regime map placement to term balance

If groups are slow:
- Skip full ranking detail for Scenario C and focus on dominant balance only

---

## Exercise 1: Expected Answers

### $\rho \frac{\partial \mathbf{V}}{\partial t}$
- Meaning: Local acceleration due to time variation at a fixed point
- Cause: Flow conditions changing with time
- Effect: Unsteady inertia contribution
- Units: $\rho U/T \sim \mathrm{kg/m^3}\cdot\mathrm{m/s^2}=\mathrm{N/m^3}$

### $\rho(\mathbf{V}\cdot\nabla)\mathbf{V}$
- Meaning: Convective acceleration from spatial velocity variation along trajectories
- Cause: Fluid moving into regions with different velocity
- Effect: Nonlinear inertia, curvature and shear-driven acceleration
- Units: $\rho U^2/L = \mathrm{N/m^3}$

### $-\nabla p$
- Meaning: Pressure-force per unit volume
- Cause: Pressure gradients
- Effect: Drives/retards flow from high to low pressure
- Units: $\mathrm{Pa/m}=\mathrm{N/m^3}$

### $\mu\nabla^2\mathbf{V}$
- Meaning: Viscous diffusion of momentum
- Cause: Velocity curvature and molecular momentum transport
- Effect: Smooths velocity gradients, dissipates kinetic energy
- Units: $\mu U/L^2 = \mathrm{Pa\cdot s}\cdot\mathrm{m/s}/\mathrm{m^2}=\mathrm{N/m^3}$

### $\rho\mathbf{g}$
- Meaning: Body force from gravity
- Cause: Mass in gravitational field
- Effect: Hydrostatic pressure variation, buoyancy-related forcing
- Units: $\mathrm{kg/m^3}\cdot\mathrm{m/s^2}=\mathrm{N/m^3}$

### $\nabla\cdot\mathbf{V}=0$
- Meaning: Incompressibility constraint (no volumetric dilation)
- Cause: Constant density assumption for fluid parcel
- Effect: Kinematic closure and coupling among velocity components
- Units: $1/\mathrm{s}$ and equals zero

Common misconception to address:
- Students often say "incompressible means pressure is constant". Clarify that incompressibility does not imply uniform pressure.

---

## Exercise 2: Suggested Rankings and Balances

Note:
- Accept defensible alternatives if scaling logic is clear.
- Emphasize "dominant" does not mean "only".

### Scenario A: Pump switched off in long pipeline
Typical expected ranking:
1. $\rho \frac{\partial \mathbf{V}}{\partial t}$
2. $-\nabla p$
3. $\mu\nabla^2\mathbf{V}$
4. $\rho(\mathbf{V}\cdot\nabla)\mathbf{V}$
5. $\rho\mathbf{g}$ (if mostly horizontal line)

Likely dominant balance:
- Unsteady inertia balanced by pressure gradient and viscous resistance during decay

Acceptable discussion points:
- If line is steeply inclined, gravity term can move up in rank
- At high initial flow speed, convective term may briefly matter

### Scenario B: High-speed flow through sharp 90 degree bend
Typical expected ranking:
1. $\rho(\mathbf{V}\cdot\nabla)\mathbf{V}$
2. $-\nabla p$
3. $\mu\nabla^2\mathbf{V}$
4. $\rho \frac{\partial \mathbf{V}}{\partial t}$ (steady operation assumption)
5. $\rho\mathbf{g}$

Likely dominant balance:
- Convective inertia balanced mainly by pressure gradient, with viscous effects secondary (except near walls)

Acceptable discussion points:
- Near-wall subregion can be viscosity-influenced despite high bulk Reynolds number

### Scenario C: Nearly still water in tall vertical tank
Typical expected ranking:
1. $-\nabla p$
2. $\rho\mathbf{g}$
3. $\mu\nabla^2\mathbf{V}$
4. $\rho \frac{\partial \mathbf{V}}{\partial t}$
5. $\rho(\mathbf{V}\cdot\nabla)\mathbf{V}$

Likely dominant balance:
- Hydrostatic balance: $\nabla p \approx \rho \mathbf{g}$

Acceptable discussion points:
- In strict static equilibrium, velocity terms and viscous term are negligible

---

## Exercise 3: Dimensionless Interpretation Key

Expected core meaning:
- High $Re$: inertia dominates viscous effects in bulk flow
- Low $Re$: viscous effects dominate
- High $St$: strong unsteady behavior relative to advection timescale
- Low $St$: quasi-steady behavior
- Low $Fr$: gravity important relative to inertia
- High $Fr$: inertia more important than gravity
- High $Eu$: strong pressure forces relative to dynamic pressure scale

Suggested scenario placement:
- Scenario A: moderate $Re$, moderate to high $St$, moderate $Fr$
- Scenario B: high $Re$, low $St$ if operating steadily, high $Fr$
- Scenario C: very low characteristic $U$ implies very low $Fr$, near-static interpretation

What to look for in good student maps:
- Placement justified with words and scaling, not only symbols
- Explicit link from map location to term balance

---

## Quick Debrief Prompts (2 min)
- Which term was easiest to visualize physically and why?
- Where did two groups disagree most in ranking?
- What additional data would reduce ranking uncertainty?

## Optional Extension (if 5 extra min)
Ask groups to propose one engineering flow from their discipline and state a first-pass dominant balance using the same framework.
