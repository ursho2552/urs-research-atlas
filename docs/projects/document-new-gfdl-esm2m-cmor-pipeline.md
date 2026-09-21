# GFDL-ESM2M CMOR pipeline

<div class="ra-page ra-simple-page" markdown="1">

<span class="ra-badge ra-badge-active">active</span>

**Area:** Climate data standardisation workflows  
**Updated:** 2026-09-21 07:46  
**Tags:** `GFDL-ESM2M` `CMOR` `CMIP` `climate data` `NetCDF` `metadata` `Python`

## Summary

For the TipMIP-ESM project, we need to provide our simulation data in a CMIP standardised format. For the deliverables, the simulations should be in *CMIP6Plus* format. To this end, we developed a custom *Climate Model Output Rewriter" (CMOR) pipeline for our model GFDL-ESM2M.

Previously, this tools was part of a larger ocean tools repository. However, the tool got very large and complex, which then resulted in the creation of a separate repository for the tool alone, and a refactoring. During the refactoring, the tool was made more general to allow for the use of different CMIP formats, but stayed specific to GFDL-ESM2M output.

As the tool might be used in the future for other projects, it is important to write a comprehensive and complete documentation of the tool with practical examples and detailed explanations. In addition, the tool should be tested against the old pipeline to ensure consistency. Afterwards, new tests should be written to allow easy and reproducible extensions of the pipeline in the future.


## Progress

<div class="ra-progress"><div class="ra-progress-bar" style="width: 88%"></div></div>

7 / 8 tasks completed.

## Tasks

| Done | Task | Status | Priority | Due date |
| --- | --- | --- | --- | --- |
| ✅ | Test new version | done | medium | 2026-09-30 |
| ✅ | Add CMIP6 Tables | done | medium | — |
| ✅ | Write tests for functions | done | medium | — |
| ✅ | Test corrected pipeline across systems | done | medium | — |
| ✅ | Re-run pipeline with updated variable tables | done | medium | — |
| ✅ | Test new bug fix for hfbasin | done | high | 2026-09-21 |
| ⬜ | Transfer corrected data to SPIRIT and DKRZ | in_progress | high | 2026-09-25 |
| ✅ | CMORize output with corrected pipeline | done | high | 2026-09-25 |

## Updates


### Data transfer

**2026-09-21 07:46**

The CMIP piControl-spinup, TIPMIP and TIPMIP-OCN simulations are now being transferred to SPIRIT and DKRZ




### Branches re-done

**2026-09-17 11:52**

The following branches have been run:

**TIPMIP-SOCN**: 

- tipmip-ocn-p1t1-Aa
- tipmip-ocn-p1t1-Ab
- tipmip-ocn-p1t2-Aa
- tipmip-ocn-p1t2-Ab

**TIPMIP-OCN**: 

- tipmip-ocn-p1t1-Aa
- tipmip-ocn-p1t1-Ab
- tipmip-ocn-p1t1-Ac
- tipmip-ocn-p1t1-Ad
- tipmip-ocn-p1t2-Aa
- tipmip-ocn-p1t2-Ab
- tipmip-ocn-p1t2-Ac
- tipmip-ocn-p1t2-Ad

**TIPMIP**:

- esm-piControl-spinup
- esm-piControl
- esm-up2p0
- esm-up2p0-gwl2p0
- esm-up2p0-gwl2p0-50y-dn2p0
- esm-up2p0-gwl2p0-50y-dn2p0-gwl0p0
- esm-up2p0-gwl4p0 
- esm-up2p0-gwl4p0-50y-dn2p0
- esm-up2p0-gwl4p0-50y-dn2p0-gwl0p0
- esm-up2p0-gwl4p0-50y-dn2p0-gwl2p0





### Corrected bugs and improved efficiency

**2026-09-16 14:55**

Several bugs were found during a code review.

After the review the pipeline was very slow. As such, I changed the orchestrating script to reduce the runtime




### Added exception to pipeline

**2026-09-14 16:09**

The pipeline would fail if only one of the several input files were missing. However, it should still run on the available files.
As such, it now throws a warning when a file is missing, and during processing checks if a specific file an year are present. If the files are missing, that file and year are skipped.




### Run with updated variable tables

**2026-09-11 11:28**

The cmor pipeline was now run across different systems for TIPMIP-ESM and TIPMIP-OCN simulations.




### Found small unit errors in CMIP variable definitions

**2026-09-10 17:06**

Some units for the atmosphere, ocean, and land did not match the metadata. For the sea ice, one variable had to be swapped, as it was not the correct one.




### Added tests to CMOR pipeline

**2026-09-09 16:14**

Added tests to functions used in the CMOR pipeline. In doing this, several bugs were found and corrected.




### Testing with TIPMIP-OCN

**2026-09-09 13:03**

To test portability across systems, the tool is currently being tested on UBELIX for the TIPMIP-OCN simulations




### Tested new version

**2026-09-07 16:52**

New version finishes without problems for the TIPMIP-ESM simulations, and results in the finished file structure.




### Added CMIP6 tables

**2026-09-07 16:52**

Added older CMIP6 tables to the repository, in case this format is used.




### Testing new version

**2026-09-02 17:14**

Changed how time is handled for very long simulations and adapted where the plevel transformation/interpolation is done with respect to the output directory.

The new pipeline is currently being tested for the TIPMIP-ESM simulations.




### Running TIPMIP-OCN test

**2026-08-03 10:27**

Rerunning the current pipeline on TIPMIP-OCN experiment A simulations to test the outcome and structure




</div>
