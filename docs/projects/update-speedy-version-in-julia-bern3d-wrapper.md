# Update Speedy version in Julia Bern3D wrapper

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Research software maintenance  
**Updated:** 2026-08-11 10:21  
**Tags:** `SpeedyWeather` `Julia` `model coupling` `Bern3D`

## Summary

The Bern3D model has a relatively simple atmosphere module. To improve this, we decided to couple a new and highly customisable atmospheric model called SpeedyWeather (Klöwer et al., 2024). Furthermore, this new coupled model will be used in subsequent projects that try do use online downscaling to couple the Bern3D-SpeedyWeather model to a land vegetation model LPX, which requires finer-scale inputs than what Bern3D is currently able to provide.

Previously, we successfully coupled Bern3D's ocean to SpeedyWeather using v0.18. However, new breaking changes have been implemented with v0.21.1, and as this project is ongoing, we would like to continuously keep up our coupling with the newest SpeedyWeather version available. As such, we need to update SpeedyWeather to the newest release in our shared environment. Second, we need to revise  the breaking changes and implement them into our coupling.


In addition, we noticed that our freshwater coupling has a missing component, the river runoff. For this reason, we will try to reimplement the freshwater coupling. 


Bibliography:

- Klöwer et al., (2024). SpeedyWeather.jl: Reinventing atmospheric general circulation models towards interactivity and extensibility. Journal of Open Source Software, 9(98), 6323, doi:10.21105/joss.06323.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 75%"></div></div>

3 / 4 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Update SpeedyWeather to newest release | done | medium | — |
| ✅ | Implement breaking changes into current coupling | done | medium | — |
| ✅ | Implement land runoff into freshwater coupling | done | high | — |
| ⬜ | Test new coupled model | in_progress | high | — |

## Updates


### Current status

**2026-08-11 10:21**

In the current version, the overall patterns look reasonable. The old waters in the Pacific are located at 1500-2500 m depth at around 20-45°N. The SST and SSS patterns look right, with the Mediterranean and subtropical salinity maxima, fresh subpolar and Arctic waters, and sensible SST gradients. The AMOC strength is a bit weaker than in the standard run, stabilising at around 20 Sv.

After 1190 simulation years, we find the following:

- Global salinity has a drift of −0.100813 -> −0.100394, drift 3.5e-7 /yr ,
- Applied heat is −0.086 W/m² -> −0.00018 K/yr,
- The sea ice extent is roughly 5.12% of the ocean (18.781 10$^6$ km$^2$),
- The global temperature stabilises at 3.95°C,
- The AMOC strength stabilises at 20 Sv,


However, this balance may be due to the wrong reason. Ice production is 8 times higher than observed. Speedy applies -5.18 W/m$^2$, from which most of it is directly converted into sea ice (freeze clip = 5.09 W/m$^2$). There is also a cooling atmosphere bias, which is absorbed by the ice cycle. This increased ice cycle explains the fresher salinity and overall lower SST




<div class="ra-gallery-grid">
<figure class='ra-figure'><img class='ra-lightbox-image' src='../../assets/uploads/update-speedy-version-in-julia-bern3d-wrapper/updates/2026-08-11-1021-sst-sss.png' alt='Sea Surface Temperature (SST in °C) and Sea Surface Salinity (SSS in PSU) of the Bern3D-SpeedyWeather coupled model after 1190 simulation years. '><figcaption>Sea Surface Temperature (SST in °C) and Sea Surface Salinity (SSS in PSU) of the Bern3D-SpeedyWeather coupled model after 1190 simulation years. </figcaption></figure>
</div>



### Fix conservation and stability in SpeedyWeather-Bern3D coupling

**2026-08-07 16:44**

Freshwater: use ocean (not grid-total) humidity flux for evaporation, weight runoff by land fraction, and close the global water budget. Fixes the ~3.6 Sv spurious input that drove the salinity drift.

Brine: split sea-ice salt flux (1-f) surface / f depth as atmOAhFWfl.f90 does, and exclude it from the water-cycle closure. It was applied twice.

Wind stress: set dztau/dztav as well as tau, so baroclinic and barotropic forcing are consistent; read scf from the parameter file instead of hardcoding
1.8; low-pass to climatology-like smoothness.

Remapping: ocean-aware weights with both land-sea masks built in, so flux is no longer discarded on Bern3D land (~5.9% of ocean area).

Heat: correct the freezing bound coefficient, apply it after the closure, and report true annual means instead of a once-a-year sample that aliased onto the seasonal cycle.





### Re-implemented conservative remapping

**2026-08-06 16:23**

The remapping from Bern3D to SpeedyWeather's grid was not conserving mass nor fluxes.

I have now reimplemented it, and added diagnostics to continuously check that the fluxes and masses are conserved before and after the remapping. In addition, I now also added a surface runoff routing with a 3x3 stencil to the coupler analogously to how the surface runoff is handled in Bern3D with a fraction routed to the coast and the rest to a *global* bucket that is then distributed.




### Bug in Speedy river runoff

**2026-08-04 16:32**

When implementing runoff into the freshwater flux, I encountered a bug in the current SpeedyWeather release v0.21.1.

In `soil_moisture.jl`, the river runoff accumulation in the `land_bucket_soil_moisture_kernel` appears wrong. The implementation currently uses:
```
R[ij] += Δt * (1 - p) * δW₁ * f₁,
```
which based on the units used in the kernel, results in R having the units `m s` rather than `s`, i.e., the magnitude of the runoff scales with the timestep rather than the precipitation. This also explains why the river runoff is so much higher than `rain_large_scale`, `rain_convection`, and `snow_large_scale`.

To test this, I created a branch, where the runoff is now calculated using:
```
R[ij] += (1 - p) * δW₁ * f₁ 
```
which results in runoff values that are at least comparable to the other freshwater accumulators






### Update to new version

**2026-08-03 11:21**

The update of SpeedyWeather to the newest version was not straight forward. 

A simple `Pkg.update` would not work due to dependencies being preserved. Instead we used `Pkg.update("SpeedyWeather"; preserve=Pkg.PRESERVE_NONE)`




</div>
