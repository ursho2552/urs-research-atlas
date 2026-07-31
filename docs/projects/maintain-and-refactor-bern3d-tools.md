# Maintain and refactor Bern3D Tools

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Research software engineering  
**Updated:** 2026-07-31 11:09  
**Tags:** `Python` `Bern3D` `workflow automation` `research software`

## Summary

Develop and maintain tools for repetitive Bern3D workflows such as spin-up runs, sensitivity analysis, Latin hypercube sampling, and model-output analysis. The tools should be refactored to become more user-friendly, customizable, and reproducible, with the long-term goal of delivering them as a shareable Python package.

## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 25%"></div></div>

1 / 4 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Refactor Bayesian Optimization module | done | medium | — |
| ⬜ | Refactor Sensitivity analysis module | todo | low | — |
| ⬜ | Refactor LHS module | todo | low | — |
| ⬜ | Refactor Spinup module | todo | low | — |

## Updates


### Corrected bug in Bayesian optimization module

**2026-07-31 11:08**

A bug in the npzd optimizer was fixed. The error occurred when 2D NPZD fields were loaded and compared with expected values. Before, the tool tried to take the last time-step, however, this had been selected before. This resulted in the tool only taking the longitudes for calculating the error




</div>
