# MHW under transient and stable conditions

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-completed">completed</span>

**Area:** Climate data processing  
**Updated:** 2026-10-21 12:09  
**Tags:** `Python` `GFDL-ESM2M` `netCDF`

## Summary

For a chapter on marine heatwaves, we will analyse how marine heatwave characteristics differ under transient temperature conditions compared to long term stable temperature conditions. To this end, we will use AERA simulations with different temperature targets.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 100%"></div></div>

4 / 4 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Calculate threshold from historical ensemble data | done | high | 2026-10-14 |
| ✅ | Identify MHW for each temperature target during the transient period | done | high | 2026-10-17 |
| ✅ | Identify MHW for each temperature target during end of stability period | done | high | 2026-10-17 |
| ✅ | Calculate MHW masks for all years | done | high | 2026-10-23 |

## Updates


### Established when simulations reach ocean temperature stability

**2026-10-19 12:08**

Determined the first year when the 31-year running mean of the derivative of the global ocean temperature time series reaches stability (<0.0001 K/a).


<div class="ra-gallery-grid">
<figure class='ra-figure'><img class='ra-lightbox-image' src='../../assets/uploads/mhw-under-transient-and-stable-conditions/updates/2026-10-19-1208-ocean-temp-stability.png' alt='Derivative of the global volume-weighted ocean temperature for five ensemble members across three global warming levels (black). the vertical dashed lines show the average year in which the ensemble members reach stability on a 31-year running mean (colored lines).'><figcaption>Derivative of the global volume-weighted ocean temperature for five ensemble members across three global warming levels (black). the vertical dashed lines show the average year in which the ensemble members reach stability on a 31-year running mean (colored lines).</figcaption></figure>
</div>



### Established when simulations reach global warming level

**2026-10-19 12:04**

Determined the first year when a 31-year running mean of the 2 m air temperature reaches the global warming level of 1.5, 2.0, and 3.0°C


<div class="ra-gallery-grid">
<figure class='ra-figure'><img class='ra-lightbox-image' src='../../assets/uploads/mhw-under-transient-and-stable-conditions/updates/2026-10-19-1204-gwl-stability.png' alt='Global 2 m air temperature for five ensemble members across three global warming levels (black). the vertical dashed lines show the average year in which the ensemble members reach the global warming level on a 31-year running mean (colored lines).'><figcaption>Global 2 m air temperature for five ensemble members across three global warming levels (black). the vertical dashed lines show the average year in which the ensemble members reach the global warming level on a 31-year running mean (colored lines).</figcaption></figure>
</div>



### Building timeseries

**2026-10-16 13:55**

The global atmospheric time series and global ocean temperature are being calculated. The temporal evolution of these will be used to determine the year in which the warming level with respect to pre-industrial conditions is reached for each ensemble member, and the year in which the temperature in the ocean reaches equilibrium.




</div>
