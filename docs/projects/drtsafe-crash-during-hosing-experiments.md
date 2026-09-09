# DRTSafe crash during hosing experiments

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** GFDL-ESM2M  
**Updated:** 2026-09-08 17:37  
**Tags:** `Fortran` `hosing experiments`

## Summary

When using hosing experiment following the NaHOSMIP protocol, the simulations with GFDL-ESM2M crash. The crash occurs at the same position in the Arctic at (i,j) = (75, 198). 

We noticed that there appear to be some instabilities in salinity and temperature at depth. From one depth level to the next, the temperature can oscillate between +10°C and -10°C. These oscillations usually start roughly two days before the crash.

We traced the error to the piecewise parabolic method advection scheme (function advect_tracer_mdppm in the ocean_tracer_advect.F90 module). This function tries to keep the tendency in temperature and salinity within some boundaries. However, if these boundaries become very narrow, small overshoots may occur and accumulate over time, which ultimately leads to the large instabilities.

To avoid this crash, the usual solution is to restart the failed simulation year with a small perturbation.

The goal of this project is to inspect why this crash occurs, find possible solutions, implement them, and test them for future hosing simulations.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>

0 / 1 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ⬜ | Diagnose why the crash occurs | in_progress | low | — |

## Updates


### DRTsafe crash during high-latitude hosing experiments

**2026-09-08 17:37**

Uniform freshwater hosing experiments (>50°N) in GFDL-ESM2M crash reliably around year-day 10-25 with *drtsafe: root not bracketed* in TOPAZ's carbonate chemistry (*FMS_ocmip2_co2calc.F90*), triggered by temperature/salinity reaching unphysical values. Root cause has been identified with high confidence; it is a structural property of the model's B-grid discretization, not a fixable code defect, so we are not pursuing a deterministic fix. Current mitigation is restarting from Jan 1 with a small (~10⁻¹² K) perturbation to the lowest atmospheric level until a run completes.

**Root cause:**

- The drtsafe failure is a downstream symptom: unphysical T/S reach TOPAZ once a genuine ocean dynamical instability has already run away.
- The actual instability is a B-grid "gravity wave null mode" (checkerboard noise) in the barotropic/free-surface solver — a documented pathology of this grid family (confirmed both in the code's own comments and independently: MOM6 moved to C-grid specifically to avoid it).
- It is consistently anchored at grid point (75,198) / ~86.4°N, 104.5°E — one row from the tripolar grid's FOLD_NORTH_EDGE seam, a numerically delicate part of the domain, where grid cells are also ~25% smaller than mid-latitude and a moderate local bathymetric gradient exists.
- The hosing forcing itself was verified clean: uniform at the source, and correctly/gently distributed over its 40 m insertion depth (magnitude ~2.6 ppm of a grid cell's mass per timestep) — not an independent contributor.
- Confirmed the instability is marginal/chaotic, not deterministic: a round-off-level (10⁻¹² K) perturbation to the atmosphere restart state changes whether a given run crashes at all, which might be evidence that the system sits on a bifurcation, not near one with exploitable margin.

**What was tried and ruled out as a full fix:**

- CFL clamp in the tracer advection scheme (advect_tracer_mdppm) 
- Global barotropic damping, both Laplacian and biharmonic families
- Finer barotropic sub-stepping (barotropic_split 80→120→250) 
- Spatially localized damping patch at the fold 




</div>
