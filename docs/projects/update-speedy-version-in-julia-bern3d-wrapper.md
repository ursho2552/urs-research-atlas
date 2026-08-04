# Update Speedy version in Julia Bern3D wrapper

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Research software maintenance  
**Updated:** 2026-08-04 16:32  
**Tags:** `SpeedyWeather` `Julia` `model coupling` `Bern3D`

## Summary

The version of SpeedyWeather has changed with some breaking changes.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 67%"></div></div>

2 / 3 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Update SpeedyWeather to newest release | done | medium | — |
| ✅ | Implement breaking changes into current coupling | done | medium | — |
| ⬜ | Implement land runoff into freshwater coupling | in_progress | high | — |

## Updates


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
