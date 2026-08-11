# Atmospheric CO2 constraint for AERA

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate target modelling  
**Updated:** 2026-08-11 16:16  
**Tags:** `AERA`

## Summary

This project aims at extending AERA by introducing a second target based on the global surface ocean aragonite saturation state, in addition to the existing global mean surface temperature target.

For this new target, we use atmospheric CO$_2$ content rather than cumulative emissions to determine allowable future emissions. This is necessary because, once the target is reached, the ocean and land continue to absorb atmospheric CO$_2$ . As atmospheric CO$_2$  declines, some additional emissions may therefore become compatible with maintaining the prescribed aragonite saturation state.

To account for this, we implemented a new constraint based on atmospheric carbon content. The framework determines the atmospheric CO$_2$  level associated with the target aragonite saturation state and uses its subsequent evolution to derive allowable future emissions. This allows emissions to respond dynamically to continued land and ocean carbon uptake after the target has been reached.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 83%"></div></div>

5 / 6 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Find bug resulting in differences between single and combined target | done | medium | — |
| ✅ | Implement ocean/land sink | done | medium | — |
| ✅ | Change driver used to estimate future emissions | done | medium | — |
| ✅ | Calculate atmospheric CO2 content from historical simulation | done | medium | 2026-08-07 |
| ✅ | Implement new column in AERA for atmospheric CO2 content and feedback from model simulation | done | medium | 2026-08-07 |
| ⬜ | Test new implementation | in_progress | medium | 2026-08-14 |

## Updates


### Testing the new implementation

**2026-08-11 16:16**

The new implementation is now being tested on CSCS. 

After fixing some problems in the setup and run-scripts, the model appears to run smoothly, with updated emission fields derived from the atmospheric carbon content and the land/ocean sink.




### Running offline tests

**2026-08-10 16:12**

I have now implemented the use of atmospheric C content for estimating future emissions until a certain $\Omega$ target is reached. This is currently done without any real feedback from the model. This is done as follows:

1. Run AERA on 2026 creating an emissions file,
2. Copy simulation files from an existing run
3. After each run, save the Omega values
4. On the next stocktake, run AERA again

This is done to check whether the pipeline would run, and to see the emissions and file structure created. The model response will be wrong, as the emissions used in the actual model run stem from the old AERA implementation that used cumulative emissions instead of the atmospheric C content.





### Update in AERA code worked

**2026-07-29 10:37**

Marine tested the new setup on CSCS for 10 years. The simulations are now identical when using the combined version against the single version.




### Reproducibility bug

**2026-07-28 16:11**

The reproducibility bug was caused by the combination of the meta_data.nc files. In the single target version, the  older slope parameters are stored as vectors. During the combination of the temperature and aragonite meta_data file, this structure is broken, and previous parameters are stored as scalars. This then leads to the  silent bug, where AERA does not recognise the parameters and assumes it is the first stocktake year




</div>
