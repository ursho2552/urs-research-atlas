# Re-run hosing simulations for AMOC collapse paper

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** GFDL-ESM2M  
**Updated:** 2026-08-05 15:03  
**Tags:** `hosing simulations` `GFDL-ESM2M` `CSCS`

## Summary

In GFDL-ESM2M, the standard ideal hosing routine adds tracers such as DIC and alkalinity together with the freshwater flux. While freshwater input in reality should have a certain amount of alkalinity and DIC, this may not be ideal for idealised hosing experiments, as the input of DIC and alkalinity may influence the global carbon cycle.


As such, we adapted the standard hosing routine in a separate branch (*vertical_hosing*), which adds freshwater without any tracers. The only "tracers" that may still enter the ocean are temperature and salinity. For the publication “Climate and Carbon Cycle Responses to a 21st Century AMOC Collapse under a 2 °C Stabilization Pathway” (Frölicher et al., 2026), we need to re-run the simulations with the new *vertical_hosing* branch.


Bibliography

- Frölicher, T. L., Maier, P., Burger, F. A., Silvy, Y., Swingedouw, D., & Elizondo, U. H. (2026). Climate and Carbon Cycle Responses to a 21st century AMOC collapse under a 2°C stabilization pathway. https://doi.org/10.5194/egusphere-egu26-22272

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 33%"></div></div>

1 / 3 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ⬜ | Run AERA-offline simulations | in_progress | medium | — |
| ⬜ | Run AERA online simulations | in_progress | medium | — |
| ✅ | Run recovery simulation after 100 years hosing | done | medium | — |

## Updates


### Transferred intermediate results to capacity

**2026-08-05 14:38**

The ensembles members 3 and 5 of the offline version, the recovery simulation, and the ensemble member 4 of the online version have been transferred to capacity on UBELIX




### Partial results

**2026-08-03 10:28**

Ensemble member 3 and 5 of the offline and ensemble member 4 of the online AERA version have now finished, and will be prepared for transfer to capacity storage




### Restarted both offline and online simulations

**2026-07-29 09:59**

The online simulations appear to be stuck at around the year 2166. A few ensemble members of the offline simulations are nearing the 2200 simulation year, while the others had to be reset by more than 20 years




### DRT safe crash

**2026-07-28 16:23**

The hosing simulations keep crashing in the last 100 years. 

I will keep restarting them with small perturbations until they reach at least the year 2200




</div>
