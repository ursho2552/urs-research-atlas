# ERA5 data for MHW workshop

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate data processing  
**Updated:** 2026-08-06 17:13  
**Tags:** `ERA5` `marine heatwaves` `climatology` `CDS API` `xarray` `NetCDF`

## Summary

Catherine Gregory is organising a workshop on *Understanding the dynamics and feedback mechanisms of compound heatwaves between land and ocean" (31. August to 3rd November 2026) at the University of Bern. To this end, we would like to provide some useful datasets for the participants for the hands-on parts of the workshop. 

On our cluster, we currently have ERA5 data until roughly mid 2025, but would like to update it to get the most current available fields that are necessary for the workshop. These are:

- Sea surface temperature,
- 2m temperature,
- 500 hPa geopotential height,
- U component of wind,
- V component of wind,
- Surface pressure, and
- Specific humidity.

In addition we also downloaded the UTCI, dew point, surface latent heat flux, surface sensible heat flux, surface solar radiation downwards, and surface thermal radiation downwards.

In addition, as the workshop focuses on heat waves, we would like to also provide climatologies (11-day mean), such that the participants could focus on the hands-on tasks, rather than the technical part of calculating climatologies.



## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 75%"></div></div>

6 / 8 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Update ERA5 download tool | done | medium | 2026-08-13 |
| ⬜ | Download specific humidity | in_progress | medium | 2026-08-07 |
| ✅ | Download SST | done | medium | 2026-08-07 |
| ✅ | Download 2m-temperature | done | medium | 2026-08-07 |
| ✅ | Download 500 hPa geopotential | done | medium | 2026-08-07 |
| ⬜ | Download Wind data | in_progress | medium | 2026-08-07 |
| ✅ | Download surface pressure | done | medium | 2026-08-07 |
| ✅ | Calculate climatologies | done | high | 2026-08-13 |

## Updates


### Added climatologies for different pressure levels

**2026-08-06 17:13**

New climatologies for several pressure levels were requested and calculated. In addition, the specific humidity across all pressure levels should also be downloaded for 2025 and 2026




### Missing wind fields

**2026-08-03 10:36**

All fields except the wind fields have all been downloaded




</div>
