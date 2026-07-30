# AGI on ramp-up and stability phases of TIPMIP-ESM and TIPMIP-OCN

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate model diagnostics  
**Updated:** 2026-07-30 15:56  
**Tags:** `TIPMIP` `AMOC` `AGI`

## Summary

Run our AGI pipeline on the ramp-up and stability phases of the TIPMIP-ESM and TIPMIP-OCN simulations. For the TIPMIP-OCN simulations use the tier 1 simulations (i.e., 0.3 Sv). In addition, also run the same pipeline but for TIPMIP-SOCN simulations

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>

0 / 5 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ⬜ | Run AGI pipeline on control simulation tipmip-esm-piControl or control simulation for drift | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-OCN simulations | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-ESM simulations | in_progress | medium | 2026-09-30 |
| ⬜ | Run pipeline for TIPMIP-SOCN simulations | todo | medium | 2027-02-28 |
| ⬜ | Run AGI pipeline on NASA-GISS output | todo | medium | 2026-08-07 |

## Updates


### Adjust bias correction

**2026-07-30 15:17**

Since we are using the existing pipeline for tipmip experiments rather than historical runs, we do not need to use the WOA-bias correction, which was producing empty fields for the hosing simulations. The empty fields were caused because the simulation periods did not match the WOA period.




### TIPMIP-OCN preliminary fields

**2026-07-30 09:27**

Finished calculating preliminary fields (insitu temperature and pO2) for TIPMIP-OCN simulations on UBELIX. 




### Additional setup for UBELIX

**2026-07-29 16:08**

When running the AGI pipeline on UBELIX, it appears that the following module and environmental variables need to be specified:

- module load netCDF/4.9.2-iimpi-2023a
- module load HDF5/1.14.6-gompi-2025a
- export HDF5_USE_FILE_LOCKING=FALSE




### Partial results ready

**2026-07-29 14:43**

Calculated insitu temperature and pO2 for the following TIPMIP-ESM simulations:

- piControl
- up2p0
- up2p0-gwl2p0

Combined data file with all control fields are also ready for removing model drift in other simulations




</div>
