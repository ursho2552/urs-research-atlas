# Update Speedy version in Julia Bern3D wrapper

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Research software maintenance  
**Updated:** 2026-08-03 17:04  
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
| ⬜ | Implement land runoff into freshwater coupling | todo | high | — |

## Updates


### Update to new version

**2026-08-03 11:21**

The update of SpeedyWeather to the newest version was not straight forward. 

A simple `Pkg.update` would not work due to dependencies being preserved. Instead we used `Pkg.update("SpeedyWeather"; preserve=Pkg.PRESERVE_NONE)`




</div>
