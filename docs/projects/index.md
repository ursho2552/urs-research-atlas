# Projects

<div class="ra-page ra-simple-page">
<p class="ra-lead">Browse the projects documented in this Research Atlas.</p>
<div class="ra-project-grid">
<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>AGI on ramp-up and stability phases of TIPMIP-ESM and TIPMIP-OCN</h3>
      <p class="ra-muted">Climate model diagnostics</p>
    </div>
    <span class="ra-badge ra-badge-completed">completed</span>
  </div>
  <p>This project aims at quantifying the effect of an AMOC collapse on marine ecosystems. The impact of an AMOC collapse is calculated by comparing the changes in the Aerobic Growth Index (AGI; Morée et al., 2023) relative to pre-industrial simulations (piControl). To this end, we use a set of simulations that have both gradual warming, and gradual warming with gradual freshwater hosing from the TipMIP-ESM and TipMIP-OCN projects using the GFDL-ESM2M model.

From the TipMIP-ESM project, we use the piControl simulation, the emission ramp-up simulation (*esm-up2p0*), and the stability phase (*esm-up2p0-gwl2p0*). In the ramp-up simulation, emissions are increased gradually until the global warming level reaches +2°C above pre-industrial levels in roughly 100 years. Afterwards, the simulation is branched into the stability phase, where there are 0 emissions. The stability phase runs for 250 years.

From the TipMIP-OCN project, we use similar simulations that use the same emission forcing as the *esm-up2p0* simulation, but adds a linear increase in freshwater hosing from 0 to 0.3 Sv around Greenland. We also use the same emission forcing as the *esm-up2p0-gwl2p0*, but we add a constant freshwater hosing of 0.3 Sv around Greenland for the duration of the simulation. These simulations result in a collapse/weakening of the AMOC.

In addition, we add the simulations from what we call the TipMIP-SOCN project, which is an analogue to TipMIP-OCN, but applied the hosing to the Southern Ocean rather than around Greenland.

Finally, we would like to also do a multi-model analysis of the changes in AGI by using the simulations from multiple models (e.g. NASA-GISS) in addition to our GFDL-ESM2M simulations.



Bibliography:

- Morée, A. L., Clarke, T. M., Cheung, W. W. L., and Frölicher, T. L.: Impact of deoxygenation and warming on global marine species in the 21st century, Biogeosciences, 20, 2425–2454, https://doi.org/10.5194/bg-20-2425-2023, 2023.

</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 100%"></div></div>
  <p class="ra-muted">5 / 5 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">TIPMIP</span><span class="ra-tag">AMOC</span><span class="ra-tag">AGI</span></div>
  <a class="ra-button" href="agi-on-ramp-up-and-stability-phases-of-tipmip-esm-and-tipmip-ocn/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Atmospheric CO2 constraint for AERA</h3>
      <p class="ra-muted">Climate target modelling</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Implement new feature in AERA where instead of using cumulative emissions we use atmospheric CO2 content to estimate future emissions until a specific global surface aragonite saturation state is reached</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 40%"></div></div>
  <p class="ra-muted">2 / 5 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">AERA</span></div>
  <a class="ra-button" href="atmospheric-co2-constraint-for-aera/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Bern3D documentation</h3>
      <p class="ra-muted">Scientific software documentation</p>
    </div>
    <span class="ra-badge ra-badge-paused">paused</span>
  </div>
  <p>The wiki documentation of Bern3D was very poor. Now we use Gitlab Pages and store the documentation directly on the repository. The content, however, needs to be updated and completed</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>
  <p class="ra-muted">0 / 0 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">Bern3D</span><span class="ra-tag">GitLab Pages</span><span class="ra-tag">MkDocs</span><span class="ra-tag">model documentation</span></div>
  <a class="ra-button" href="bern3d-documentation/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Couple MEDUSA to Bern3D</h3>
      <p class="ra-muted">Earth system model development</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>We got access to a new sediment model, which we would like to couple to Bern3D.</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>
  <p class="ra-muted">0 / 4 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">BERN3D</span><span class="ra-tag">MEDUSA</span><span class="ra-tag">sediment model</span><span class="ra-tag">model coupling</span><span class="ra-tag">Fortran</span><span class="ra-tag">Earth system modelling</span></div>
  <a class="ra-button" href="couple-medusa-to-bern3d/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Document new GFDL-ESM2M CMOR pipeline</h3>
      <p class="ra-muted">Climate data standardisation workflows</p>
    </div>
    <span class="ra-badge ra-badge-paused">paused</span>
  </div>
  <p>For the TipMIP-ESM project, we need to provide our simulation data in a CMIP standardised format. For the deliverables, the simulations should be in *CMIP6Plus* format. To this end, we developed a custom *Climate Model Output Rewriter&quot; (CMOR) pipeline for our model GFDL-ESM2M.

Previously, this tools was part of a larger ocean tools repository. However, the tool got very large and complex, which then resulted in the creation of a separate repository for the tool alone, and a refactoring. During the refactoring, the tool was made more general to allow for the use of different CMIP formats, but stayed specific to GFDL-ESM2M output.

As the tool might be used in the future for other projects, it is important to write a comprehensive and complete documentation of the tool with practical examples and detailed explanations. In addition, the tool should be tested against the old pipeline to ensure consistency. Afterwards, new tests should be written to allow easy and reproducible extensions of the pipeline in the future.
</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>
  <p class="ra-muted">0 / 0 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">GFDL-ESM2M</span><span class="ra-tag">CMOR</span><span class="ra-tag">CMIP</span><span class="ra-tag">climate data</span><span class="ra-tag">NetCDF</span><span class="ra-tag">metadata</span><span class="ra-tag">Python</span></div>
  <a class="ra-button" href="document-new-gfdl-esm2m-cmor-pipeline/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>ERA5 data for MHW workshop</h3>
      <p class="ra-muted">Climate data processing</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Catherine Gregory is organising a workshop on *Understanding the dynamics and feedback mechanisms of compound heatwaves between land and ocean&quot; (31. August to 3rd November 2026) at the University of Bern. To this end, we would like to provide some useful datasets for the participants for the hands-on parts of the workshop. 

On our cluster, we currently have ERA5 data until roughly mid 2025, but would like to update it to get the most current available fields that are necessary for the workshop. These are:

- Sea surface temperature,
- 2m temperature,
- 500 hPa geopotential height,
- U component of wind,
- V component of wind,
- Surface pressure, and
- Specific humidity.

In addition we also downloaded the UTCI, dew point, surface latent heat flux, surface sensible heat flux, surface solar radiation downwards, and surface thermal radiation downwards.

In addition, as the workshop focuses on heat waves, we would like to also provide climatologies (11-day mean), such that the participants could focus on the hands-on tasks, rather than the technical part of calculating climatologies.

</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 75%"></div></div>
  <p class="ra-muted">6 / 8 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">ERA5</span><span class="ra-tag">marine heatwaves</span><span class="ra-tag">climatology</span><span class="ra-tag">CDS API</span><span class="ra-tag">xarray</span><span class="ra-tag">NetCDF</span></div>
  <a class="ra-button" href="era5-data-for-mhw-workshop/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Maintain and refactor Bern3D Tools</h3>
      <p class="ra-muted">Research software engineering</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Develop and maintain tools for repetitive Bern3D workflows such as spin-up runs, sensitivity analysis, Latin hypercube sampling, and model-output analysis. The tools should be refactored to become more user-friendly, customizable, and reproducible, with the long-term goal of delivering them as a shareable Python package.</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 25%"></div></div>
  <p class="ra-muted">1 / 4 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">Python</span><span class="ra-tag">Bern3D</span><span class="ra-tag">workflow automation</span><span class="ra-tag">research software</span></div>
  <a class="ra-button" href="maintain-and-refactor-bern3d-tools/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Re-run hosing simulations for AMOC collapse paper</h3>
      <p class="ra-muted">GFDL-ESM2M</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>In GFDL-ESM2M, the standard ideal hosing routine adds tracers such as DIC and alkalinity together with the freshwater flux. While freshwater input in reality should have a certain amount of alkalinity and DIC, this may not be ideal for idealised hosing experiments, as the input of DIC and alkalinity may influence the global carbon cycle.


As such, we adapted the standard hosing routine in a separate branch (*vertical_hosing*), which adds freshwater without any tracers. The only &quot;tracers&quot; that may still enter the ocean are temperature and salinity. For the publication “Climate and Carbon Cycle Responses to a 21st Century AMOC Collapse under a 2 °C Stabilization Pathway” (Frölicher et al., 2026), we need to re-run the simulations with the new *vertical_hosing* branch.


Bibliography

- Frölicher, T. L., Maier, P., Burger, F. A., Silvy, Y., Swingedouw, D., &amp; Elizondo, U. H. (2026). Climate and Carbon Cycle Responses to a 21st century AMOC collapse under a 2°C stabilization pathway. https://doi.org/10.5194/egusphere-egu26-22272</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 33%"></div></div>
  <p class="ra-muted">1 / 3 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">hosing simulations</span><span class="ra-tag">GFDL-ESM2M</span><span class="ra-tag">CSCS</span></div>
  <a class="ra-button" href="re-run-hosing-simulations-for-amoc-collapse-paper/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Update Speedy version in Julia Bern3D wrapper</h3>
      <p class="ra-muted">Research software maintenance</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>The Bern3D model has a relatively simple atmosphere module. To improve this, we decided to couple a new and highly customisable atmospheric model called SpeedyWeather (Klöwer et al., 2024). Furthermore, this new coupled model will be used in subsequent projects that try do use online downscaling to couple the Bern3D-SpeedyWeather model to a land vegetation model LPX, which requires finer-scale inputs than what Bern3D is currently able to provide.

Previously, we successfully coupled Bern3D&#x27;s ocean to SpeedyWeather using v0.18. However, new breaking changes have been implemented with v0.21.1, and as this project is ongoing, we would like to continuously keep up our coupling with the newest SpeedyWeather version available. As such, we need to update SpeedyWeather to the newest release in our shared environment. Second, we need to revise  the breaking changes and implement them into our coupling.


In addition, we noticed that our freshwater coupling has a missing component, the river runoff. For this reason, we will try to reimplement the freshwater coupling. 


Bibliography:

- Klöwer et al., (2024). SpeedyWeather.jl: Reinventing atmospheric general circulation models towards interactivity and extensibility. Journal of Open Source Software, 9(98), 6323, doi:10.21105/joss.06323.</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 67%"></div></div>
  <p class="ra-muted">2 / 3 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">SpeedyWeather</span><span class="ra-tag">Julia</span><span class="ra-tag">model coupling</span><span class="ra-tag">Bern3D</span></div>
  <a class="ra-button" href="update-speedy-version-in-julia-bern3d-wrapper/">View project</a>
</div>
</div>
</div>
