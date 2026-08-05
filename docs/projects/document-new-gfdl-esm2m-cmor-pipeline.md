# Document new GFDL-ESM2M CMOR pipeline

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-paused">paused</span>

**Area:** Climate data standardisation workflows  
**Updated:** 2026-08-05 15:15  
**Tags:** `GFDL-ESM2M` `CMOR` `CMIP` `climate data` `NetCDF` `metadata` `Python`

## Summary

For the TipMIP-ESM project, we need to provide our simulation data in a CMIP standardised format. For the deliverables, the simulations should be in *CMIP6Plus* format. To this end, we developed a custom *Climate Model Output Rewriter" (CMOR) pipeline for our model GFDL-ESM2M.

Previously, this tools was part of a larger ocean tools repository. However, the tool got very large and complex, which then resulted in the creation of a separate repository for the tool alone, and a refactoring. During the refactoring, the tool was made more general to allow for the use of different CMIP formats, but stayed specific to GFDL-ESM2M output.

As the tool might be used in the future for other projects, it is important to write a comprehensive and complete documentation of the tool with practical examples and detailed explanations. In addition, the tool should be tested against the old pipeline to ensure consistency. Afterwards, new tests should be written to allow easy and reproducible extensions of the pipeline in the future.


## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>

0 / 0 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| — | No tasks yet | — | — | — |

## Updates


### Running TIPMIP-OCN test

**2026-08-03 10:27**

Rerunning the current pipeline on TIPMIP-OCN experiment A simulations to test the outcome and structure




</div>
