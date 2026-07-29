# Atmospheric CO2 constraint for AERA

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate target modelling  
**Updated:** 2026-07-29 10:37  
**Tags:** `AERA`

## Summary

Implement new feature in AERA where instead of using cumulative emissions we use atmospheric CO2 content to estimate future emissions until a specific global surface aragonite saturation state is reached

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 67%"></div></div>

2 / 3 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Find bug resulting in differences between single and combined target | done | medium | — |
| ✅ | Implement ocean/land sink | done | medium | — |
| ⬜ | Change driver used to estimate future emissions | todo | medium | — |

## Updates


### Update in AERA code worked

**2026-07-29 10:37**

Tested in 10 year simulation appears to work. Tested by Marine




### Reproducibility bug

**2026-07-28 16:11**

The reproducibility bug was caused by the combination of the meta_data.nc files. In the single target version, the  older slope parameters are stored as vectors. During the combination of the temperature and aragonite meta_data file, this structure is broken, and previous parameters are stored as scalars. This then leads to the  silent bug, where AERA does not recognise the parameters and assumes it is the first stocktake year




## Images

<div class="ra-gallery-grid">
<p class="ra-muted">No images yet.</p>
</div>

</div>
