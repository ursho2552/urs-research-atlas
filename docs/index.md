# Research Atlas

<div class="ra-page">

<section class="ra-hero">
  <p class="ra-eyebrow">Git-backed research showcase</p>
  <h1>Research Atlas</h1>
  <p>A local-first project showcase for researchers. Add projects, tasks, updates, and images with the local editor, then publish with GitLab Pages.</p>
  <div class="ra-actions">
    <a class="ra-button ra-button-primary" href="projects/">Explore projects</a>
    <a class="ra-button" href="todo/">View todo list</a>
    <a class="ra-button" href="gallery/">View gallery</a>
  </div>
</section>

<section class="ra-kpi-grid">
  <div class="ra-kpi-card"><span>Active projects</span><strong>5</strong></div>
  <div class="ra-kpi-card"><span>Completed projects</span><strong>0</strong></div>
  <div class="ra-kpi-card"><span>Open tasks</span><strong>15</strong></div>
  <div class="ra-kpi-card"><span>Done tasks</span><strong>5</strong></div>
</section>

<section class="ra-dashboard">
  <aside class="ra-sidebar">
    <h2>Research areas</h2>
    <ul><li>Climate data processing</li><li>Climate data standardisation workflows</li><li>Climate target modelling</li><li>Earth system model development</li><li>GFDL-ESM2M</li><li>Research software maintenance</li><li>Scientific software documentation</li></ul>
  </aside>

  <main class="ra-main">
    <h2>Featured projects</h2>
    <div class="ra-project-grid">
<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Atmospheric CO2 constraint for AERA</h3>
      <p class="ra-muted">Climate target modelling</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Implement new feature in AERA where instead of using cumulative emissions we use atmospheric CO2 content to estimate future emissions until a specific global surface aragonite saturation state is reached</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 67%"></div></div>
  <p class="ra-muted">2 / 3 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">AERA</span></div>
  <a class="ra-button" href="projects/atmospheric-co2-constraint-for-aera/">View project</a>
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
  <a class="ra-button" href="projects/bern3d-documentation/">View project</a>
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
  <a class="ra-button" href="projects/couple-medusa-to-bern3d/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Document new GFDL-ESM2M CMOR pipeline</h3>
      <p class="ra-muted">Climate data standardisation workflows</p>
    </div>
    <span class="ra-badge ra-badge-paused">paused</span>
  </div>
  <p>The custom CMOR pipeline for GFDL-ESM2M was getting too big for the shared repository with common ocean modelling scripts. Thus, I restructured it and created an independent repository. This new implementation has to be tested and properly documented for later use</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>
  <p class="ra-muted">0 / 0 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">GFDL-ESM2M</span><span class="ra-tag">CMOR</span><span class="ra-tag">CMIP</span><span class="ra-tag">climate data</span><span class="ra-tag">NetCDF</span><span class="ra-tag">metadata</span><span class="ra-tag">Python</span></div>
  <a class="ra-button" href="projects/document-new-gfdl-esm2m-cmor-pipeline/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>ERA5 data for MHW workshop</h3>
      <p class="ra-muted">Climate data processing</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Download latest data (2025 and 2026) for SST, 2m-temperature, 500 hPa geopotential height, u and v surface wind, surface pressure, and specific humidity. Afterwards, create a climatology of these fields for the period 1991-2000</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 25%"></div></div>
  <p class="ra-muted">2 / 8 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">ERA5</span><span class="ra-tag">marine heatwaves</span><span class="ra-tag">climatology</span><span class="ra-tag">CDS API</span><span class="ra-tag">xarray</span><span class="ra-tag">NetCDF</span></div>
  <a class="ra-button" href="projects/era5-data-for-mhw-workshop/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Re-run hosing simulations for AMOC collapse paper</h3>
      <p class="ra-muted">GFDL-ESM2M</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>Re-run the hosing simulations used in the publication “Climate and Carbon Cycle Responses to a 21st Century AMOC Collapse under a 2 °C Stabilization Pathway”.</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 33%"></div></div>
  <p class="ra-muted">1 / 3 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">hosing simulations</span><span class="ra-tag">GFDL-ESM2M</span><span class="ra-tag">CSCS</span></div>
  <a class="ra-button" href="projects/re-run-hosing-simulations-for-amoc-collapse-paper/">View project</a>
</div>


<div class="ra-project-card">
  <div class="ra-card-head">
    <div>
      <h3>Update Speedy version in Julia Bern3D wrapper</h3>
      <p class="ra-muted">Research software maintenance</p>
    </div>
    <span class="ra-badge ra-badge-active">active</span>
  </div>
  <p>The version of SpeedyWeather has changed with some breaking changes.</p>
  <div class="ra-progress"><div class="ra-progress-bar" style="width: 0%"></div></div>
  <p class="ra-muted">0 / 2 tasks completed</p>
  <div class="ra-tags"><span class="ra-tag">SpeedyWeather</span><span class="ra-tag">Julia</span><span class="ra-tag">model coupling</span><span class="ra-tag">Bern3D</span></div>
  <a class="ra-button" href="projects/update-speedy-version-in-julia-bern3d-wrapper/">View project</a>
</div>
</div>
  </main>

  <aside class="ra-right">
    <div class="ra-panel">
      <h2>Most urgent tasks</h2>
      
<div class="ra-list-item">
  <strong>Download SST</strong>
  <span>ERA5 data for MHW workshop · medium · due 2026-08-07</span>
</div>


<div class="ra-list-item">
  <strong>Download 2m-temperature</strong>
  <span>ERA5 data for MHW workshop · medium · due 2026-08-07</span>
</div>


<div class="ra-list-item">
  <strong>Download 500 hPa geopotential</strong>
  <span>ERA5 data for MHW workshop · medium · due 2026-08-07</span>
</div>


<div class="ra-list-item">
  <strong>Download Wind data</strong>
  <span>ERA5 data for MHW workshop · medium · due 2026-08-07</span>
</div>


<div class="ra-list-item">
  <strong>Download surface pressure</strong>
  <span>ERA5 data for MHW workshop · medium · due 2026-08-07</span>
</div>

    </div>
    <div class="ra-panel">
      <h2>Recent updates</h2>
      
<div class="ra-list-item">
  <strong>Update in AERA code worked</strong>
  <span>Atmospheric CO2 constraint for AERA · 2026-07-29 10:37</span>
</div>


<div class="ra-list-item">
  <strong>Restarted both offline and online simulations</strong>
  <span>Re-run hosing simulations for AMOC collapse paper · 2026-07-29 09:59</span>
</div>


<div class="ra-list-item">
  <strong>DRT safe crash</strong>
  <span>Re-run hosing simulations for AMOC collapse paper · 2026-07-28 16:23</span>
</div>


<div class="ra-list-item">
  <strong>Reproducibility bug</strong>
  <span>Atmospheric CO2 constraint for AERA · 2026-07-28 16:11</span>
</div>

    </div>
  </aside>
</section>

</div>
