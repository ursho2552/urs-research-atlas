# AGI on ramp-up and stability phases of TIPMIP-ESM and TIPMIP-OCN

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate model diagnostics  
**Updated:** 2026-07-29 16:08  
**Tags:** `TIPMIP` `AMOC` `AGI`

## Summary

Run our AGI pipeline on the ramp-up and stability phases of the TIPMIP-ESM and TIPMIP-OCN simulations. For the TIPMIP-OCN simulations use the tier 1 simulations (i.e., 0.3 Sv). In addition, also run the same pipeline but for TIPMIP-SOCN simulations

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>

0 / 4 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ⬜ | Run AGI pipeline on control simulation tipmip-esm-piControl or control simulation for drift | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-OCN simulations | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-ESM simulations | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-SOCN simulations | todo | medium | 2027-02-28 |

## Updates


### Additional setup for UBELIX

**2026-07-29 16:08**

When running the AGI pipeline on UBELIX, it appears that the following module and environmental variables need to be specified:

- module load netCDF/4.9.2-iimpi-2023a
- export HDF5_USE_FILE_LOCKING=FALSE




### Partial results ready

**2026-07-29 14:43**

Calculated insitu temperature and pO2 for the following TIPMIP-ESM simulations:

- piControl
- up2p0
- up2p0-gwl2p0

Combined data file with all control fields are also ready for removing model drift in other simulations




</div>
