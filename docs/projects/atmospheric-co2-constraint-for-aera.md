# Atmospheric CO2 constraint for AERA

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate target modelling  
**Updated:** 2026-07-29 12:07  
**Tags:** `AERA`

## Summary

Implement new feature in AERA where instead of using cumulative emissions we use atmospheric CO2 content to estimate future emissions until a specific global surface aragonite saturation state is reached

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 40%"></div></div>

2 / 5 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Find bug resulting in differences between single and combined target | done | medium | — |
| ✅ | Implement ocean/land sink | done | medium | — |
| ⬜ | Change driver used to estimate future emissions | todo | medium | — |
| ⬜ | Calculate atmospheric CO2 content from historical simulation | todo | medium | 2026-08-07 |
| ⬜ | Implement new column in AERA for atmospheric CO2 content and feedback from model simulation | todo | medium | 2026-08-07 |

## Updates


### Update in AERA code worked

**2026-07-29 10:37**

Marine tested the new setup on CSCS for 10 years. The simulations are now identical when using the combined version against the single version.




### Reproducibility bug

**2026-07-28 16:11**

The reproducibility bug was caused by the combination of the meta_data.nc files. In the single target version, the  older slope parameters are stored as vectors. During the combination of the temperature and aragonite meta_data file, this structure is broken, and previous parameters are stored as scalars. This then leads to the  silent bug, where AERA does not recognise the parameters and assumes it is the first stocktake year




## Images

<div class="ra-gallery-grid">
<p class="ra-muted">No images yet.</p>
</div>

</div>
