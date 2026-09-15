# Soil carbon change in TIPMIP simulations

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Earth System Modelling  
**Updated:** 2026-09-15 14:44  
**Tags:** `Fortran`

## Summary

A multi-model analysis showed that the soil carbon response in GFDL-ESM2M deviates a lot from all other models, with a very large carbon loss at higher latitudes. 

For the comparison, the processes responsible for this large increase in soil carbon need to be understood.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>

0 / 3 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ⬜ | Understand how soil carbon works in GFDL-ESM2M | in_progress | medium | 2026-09-30 |
| ⬜ | Derive drivers of the change | todo | medium | 2026-09-30 |
| ⬜ | Create documentation page for this issue | todo | medium | 2026-09-30 |

## Updates


### Possible explanation

**2026-09-15 14:44**

Todd-Brown et al., 2014 performed a multi-model analysis of CMIP5 models, which included the GFDL-ESM2MG, finding a similarly high soil carbon loss at high latitudes. 

This was attributed to the lack of permafrost dynamics in CMIP5 models.




### Understanding

**2026-09-15 14:40**

In GFDL-ESM2M, the land model LM3 from Shevliakova et al. 2009 is used.

In this model, there are two carbon pools in the soil, a fast and slow carbon pool. Both of them have a flux to the atmosphere, that is dependent on the average soil temperature and the soil moisture.




<div class="ra-gallery-grid">
<figure class='ra-figure'><img class='ra-lightbox-image' src='../../assets/uploads/soil-carbon-change-in-tipmip-simulations/updates/2026-09-15-1440-lm3-factors.png' alt='Soil carbon sink multiplier as a function of the soil temperature and soil moisture'><figcaption>Soil carbon sink multiplier as a function of the soil temperature and soil moisture</figcaption></figure>
</div>



</div>
