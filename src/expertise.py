"""Content for the "What I do" pages.

Facts and figures come from Samuel's CV and the project pages. The approach
steps describe how the work is actually done in those projects. Review and
adjust the wording freely; keep numbers tied to real work.
"""

HUB = dict(
    slug='index',
    title='What I Do & How I Work',
    tagline='From satellite data to decisions — engineered, validated and documented.',
    img='image-62',
    lead=('I build the software that sits between satellite archives and real decisions. My work spans the whole chain: '
          'finding and preparing Earth observation data, measuring change with radar and optical sensors, training models '
          'that survive contact with new places, and shipping the result as an API, an alert or a map someone can act on.'),
    why=('Most geospatial projects fail in the gaps between disciplines: a model with no reliable data pipeline, a pipeline with '
         'no validation, a validated map that never reaches the people who need it. Because I work across all of these — '
         'and maintain open-source tools for each — I can take a problem from a bounding box and a date range to a deployed, '
         'validated answer, and tell you honestly where that answer stops being reliable.'),
    process=[
        ('Start from the decision', 'Before any data is downloaded I pin down who will act on the result, what they will do with it, and how much error they can tolerate. That fixes the resolution, the sensors, the timeline and the metric that defines success.'),
        ('Get the data right', 'Federated search across 22 verified providers, checksum-verified downloads, atmospheric correction, cloud masking and STAC-catalogued, cloud-native outputs. Clean inputs prevent most downstream surprises.'),
        ('Baseline before complexity', 'A simple index, a classical InSAR chain or a ResNet-50 comes first. A foundation model or a graph network has to beat it on the same split to earn its place.'),
        ('Combine physics with learning', 'Radar and optical fusion, atmospheric corrections, physics-informed losses and multi-temporal stacks: the model respects how the sensor and the landscape actually behave.'),
        ('Validate where it is hard', 'Spatial-block and zone-based cross-validation, held-out tiles, field surveys and published references. Random splits flatter models; I test them in places they have never seen.'),
        ('Ship it and document the limits', 'APIs, alerts, dashboards, QGIS plugins and reproducible notebooks — delivered with tests, CI and a written account of what the result can and cannot support.'),
    ],
    principles=[
        ('Honest about limits', 'Caveats are part of the deliverable. In the Mexico City study I reported that the network split into 17 disconnected SBAS components, so the result is a directional check, not a validated replication.'),
        ('Open and reproducible', 'My core tools — pygeofetch, pygeovision, pyunwrap and ps-gnn — are MIT-licensed, on PyPI and archived with Zenodo DOIs. You can rerun everything.'),
        ('Validated in space, not just in time', 'Spatial cross-validation is my default, after diagnosing a crop-disease model that scored 95.8% in training but near zero on smallholder farms.'),
        ('Grounded in the field', 'Trained as a geomatic engineer, I have run GNSS, Total Station and UAV surveys myself, so validation is designed in rather than bolted on.'),
        ('Built for the end user', 'Results go where people already are: WhatsApp and SMS alerts, PDF reports, QGIS, live dashboards.'),
    ],
    engage=[
        ('Research collaboration', 'Joint work on InSAR, GeoAI, EO foundation models or validation methods — papers, datasets and open tools.'),
        ('Contract & consulting', 'Scoped projects: a pipeline, a model, a monitoring system or a feasibility study, delivered with code and documentation.'),
        ('Full-time roles', 'Geospatial software engineering, EO research engineering and GeoAI positions in Europe, Africa or remote.'),
        ('Training & capacity building', 'Through EOCoreINT: applied remote sensing and GeoAI with open tools and real West African examples.'),
    ],
)

AREAS = [
    dict(
        slug='sar-insar', icon='ICON_SAR', img='p-mexico-lg',
        title='SAR & InSAR',
        tagline='Millimetre-scale ground motion from radar — measured, corrected and honestly reported.',
        lead=('Radar satellites see through cloud and darkness, and interferometric SAR (InSAR) turns the phase difference between '
              'acquisitions into ground displacement. I build and run complete Sentinel-1 chains, from SLC search to SBAS velocity '
              'maps, for land subsidence, infrastructure stability and earthquake and volcanic deformation.'),
        deliver=[
            'Deformation velocity maps and displacement time series for your area of interest',
            'Reproducible processing pipelines you can rerun as new acquisitions arrive',
            'Quality reporting: coherence, network connectivity, baselines and where results should not be trusted',
            'Results delivered as Cloud Optimized GeoTIFF, GeoParquet time series or web-map tiles',
            'Feasibility assessments before you commit to a full processing campaign',
        ],
        audience=[
            ('Cities & utilities', 'Tracking urban subsidence from groundwater extraction, construction or reclamation.'),
            ('Infrastructure owners', 'Screening roads, dams, embankments and mine sites for slow, hidden movement.'),
            ('Hazard & research teams', 'Measuring deformation after earthquakes and eruptions with a reproducible chain.'),
            ('Tropical-region programmes', 'Where persistent cloud cover makes optical monitoring unreliable.'),
        ],
        approach=[
            ('Define the motion that matters', 'Expected rate, spatial extent and the decision it informs. These set the stack length, acquisition geometry and the choice between SBAS and persistent-scatterer methods.'),
            ('Check feasibility before processing', 'Preflight checks on AOI coverage, network connectivity and perpendicular and temporal baselines catch a doomed stack before compute is spent.'),
            ('Process with the physics corrected', 'Orbit-based coregistration with per-burst Enhanced Spectral Diversity, flat-earth and topographic phase removal, ERA5 tropospheric and IONEX ionospheric correction.'),
            ('Unwrap with the right tool for each region', 'SNAPHU by default; pyunwrap\'s learned unwrapper where low coherence defeats it. Each region is routed to the method that benchmarks stronger, rather than claiming one method always wins.'),
            ('Invert and select scatterers', 'SBAS inversion to velocities and time series; graph-neural-network persistent-scatterer selection (ps-gnn) for irregular urban targets.'),
            ('Validate and state the limits', 'Compare with published references, GNSS or levelling where available, and report network fragmentation and coherence gaps alongside the map.'),
        ],
        evidence=[('67', 'Sentinel-1 SLC scenes processed for Mexico City'), ('2,211 → 78', 'Candidate pairs screened to valid interferograms'),
                  ('−35.5 cm/yr', 'Recovered, vs a published −39.1 cm/yr peak'), ('3', 'Deformation events run through the same chain')],
        evidence_note='Mexico City subsidence, the 2021 Piton de la Fournaise eruption and the 2016 Amatrice earthquake were processed with the same pygeofetch InSAR chain.',
        projects=['pyunwrap', 'ps-gnn', 'mexico-city-subsidence', 'urban-subsidence-watcher'],
        tools=['Sentinel-1 SLC', 'ASF Vertex API', 'Copernicus Data Space', 'SNAPHU', 'SBAS', 'ERA5', 'IONEX', 'pygeofetch', 'pyunwrap', 'ps-gnn', 'GDAL / Rasterio'],
        different=[
            ('I report the network, not just the map', 'Connectivity, coherence and fragmentation are part of every deliverable, so you know how far to trust each pixel.'),
            ('Hybrid, not dogmatic', 'Classical and learned unwrapping are combined region by region, based on benchmarks rather than preference.'),
            ('Built on my own open chain', 'The full Sentinel-1 workflow lives in pygeofetch, CI-tested and archived with a DOI, so results can be reproduced.'),
        ],
        faq=[
            ('How long a time series do I need?', 'It depends on the rate you expect. Fast subsidence of several centimetres a year shows within months; slow millimetre-scale motion needs longer stacks. I size this during the feasibility step, before processing.'),
            ('Does InSAR work over vegetation?', 'C-band coherence drops over dense vegetation, so I check coherence early, focus on built-up or bare targets where needed, and state clearly where the signal is not usable rather than interpolating over it.'),
            ('What will I actually receive?', 'Velocity and displacement rasters (GeoTIFF / COG), time series as CSV or GeoParquet, the notebooks or pipeline configuration used, and a short technical note covering quality and limitations.'),
        ],
    ),
    dict(
        slug='geospatial-ai', icon='ICON_AI', img='p-atewa-lg',
        title='Geospatial AI & Computer Vision',
        tagline='Models that hold up outside the training tiles.',
        lead=('From crop types and illegal mining to building footprints and plant counts, I design deep-learning systems for '
              'satellite, aerial and drone imagery, and I judge them by how they perform in places they have never seen.'),
        deliver=[
            'Segmentation, detection and classification models trained for your imagery and classes',
            'Benchmarks against simple baselines, so the added complexity is justified',
            'Spatially honest accuracy reports with uncertainty, not just a headline score',
            'Inference pipelines from search to finished map, mask or dataset',
            'Deployment artifacts: ONNX models, FastAPI / WebSocket inference servers, edge-ready exports',
        ],
        audience=[
            ('Agriculture & food security', 'Crop-type maps, crop condition and plant counting for smallholder and commercial farms.'),
            ('Forest & mining monitoring', 'Detecting illegal mining, deforestation and land-cover change under persistent cloud.'),
            ('Governments & NGOs', 'Land-cover, building and change maps that stand up to scrutiny.'),
            ('Teams with a model that fails in the field', 'Diagnosing domain shift, label problems and leakage in existing models.'),
        ],
        approach=[
            ('Start from the decision, not the architecture', 'Which map, at what resolution, with what error is acceptable, and who will act on it. That defines the classes, the metric and the validation design.'),
            ('Audit the data and labels', 'Check sources, label noise and class balance; mining scars, for example, covered under 4% of the Atewa landscape. Where labels are scarce, bootstrap them from OpenStreetMap, building footprints, ESA WorldCover, Dynamic World, SAM or UAV imagery.'),
            ('Baseline first', 'Train a ResNet-50 or U-Net baseline before reaching for foundation models. A complex model must beat a simple one on the same spatial split.'),
            ('Fit the model to the physics', 'SAR–optical fusion for cloud-prone regions, multi-temporal stacks for crops, EO foundation models (Clay, Prithvi-EO-2.0, DINOv3) where they add value, and imbalance-aware losses such as focal, Tversky and OHEM with hard negative mining.'),
            ('Validate spatially', 'Spatial-block or agro-ecological-zone cross-validation, held-out tiles and field re-validation. Random pixel splits overstate accuracy because neighbouring pixels are nearly identical.'),
            ('Deploy and keep watching', 'Export to ONNX, serve through FastAPI with batch and WebSocket inference, and monitor drift, with Grad-CAM, SHAP and uncertainty estimates to explain predictions.'),
        ],
        evidence=[('82% / 0.79', 'Recall / F1 for illegal-mining detection on held-out tiles'), ('> 0.70', 'F1 for 10 m crop types under spatial cross-validation'),
                  ('95.8%', 'In-domain score of a crop-disease CNN that failed on smallholder farms, diagnosed and fixed'), ('119+', 'Architectures registered in pygeovision')],
        evidence_note='The crop-disease model scored 95.8% in its training domain but close to zero on smallholder farms; geographically stratified data diversification and field re-validation resolved it.',
        projects=['ps-gnn', 'pyunwrap', 'atewa-mining-detector', 'crop-type-mapping-clay'],
        tools=['PyTorch', 'PyTorch Geometric', 'TensorFlow', 'U-Net', 'SegFormer', 'Swin-UNETR', 'YOLOv8', 'Clay', 'Prithvi-EO-2.0', 'DINOv3', 'SAM', 'ONNX', 'Optuna', 'pygeovision'],
        different=[
            ('Spatial cross-validation by default', 'Every reported score comes from areas the model did not train on.'),
            ('I go looking for failure', 'Domain shift, leakage and label noise are tested for directly, because that is where field deployments break.'),
            ('Uncertainty is a feature', 'Ensemble and Bayesian uncertainty flag the predictions that need a human look.'),
        ],
        faq=[
            ('How many labels do I need?', 'Often fewer than you think. Foundation models and automated labelling from open datasets reduce the annotation burden; I estimate the need after auditing your data and target classes.'),
            ('Should we use a foundation model?', 'Sometimes. They help most when labels are scarce or regions vary widely. I benchmark them against a simple baseline on the same spatial split and recommend whichever performs better for the cost.'),
            ('Can the model run offline or on the edge?', 'Yes. Models can be exported to ONNX and sized for edge hardware; the Urban Subsidence Watcher uses a deliberately small U-Net for this reason.'),
        ],
    ),
    dict(
        slug='eo-data-engineering', icon='ICON_DATA', img='image-63',
        title='EO Data Engineering',
        tagline='Reliable pipelines from satellite archives to analysis-ready data.',
        lead=('Most Earth observation projects lose weeks to finding, downloading, correcting and formatting data. I build the '
              'infrastructure that turns that into one command: federated search, verified downloads, processing and '
              'cloud-native outputs, all reproducible.'),
        deliver=[
            'Automated acquisition across public and commercial providers, with one interface',
            'Analysis-ready imagery: corrected, cloud-masked, reprojected and mosaicked',
            'STAC 1.0 catalogues and cloud-native outputs: COG, GeoParquet, FlatGeobuf, PMTiles',
            'Web-map delivery: tile pyramids and PMTiles from very large rasters',
            'Data-quality checks and automatic repair of common vector and raster defects',
            'Scheduled YAML pipelines with run history, tests and CI',
        ],
        audience=[
            ('Research groups', 'Who need the same data preparation to run identically for every study area and student.'),
            ('Platforms & start-ups', 'Ingesting imagery from several providers without writing a connector for each.'),
            ('Agencies with mixed archives', 'Moving from folders of GeoTIFFs to catalogued, cloud-native data.'),
            ('Web-mapping teams', 'Serving large orthomosaics and indices fast, without a tile server.'),
        ],
        approach=[
            ('Inventory the sources', 'One search across 22 verified providers, including Copernicus Data Space, USGS, NASA Earthdata, ASF, Planetary Computer, Element 84, OpenTopography, Planet and Maxar, plus a generic OGC WMS / WFS / WCS connector.'),
            ('Standardise the metadata', 'Results are normalised to STAC 1.0 with real footprint geometry and export to GeoJSON, GeoParquet or CSV, so every scene is traceable.'),
            ('Download data you can trust', 'Parallel, resumable, band-selective and checksum-verified downloads, with credentials stored encrypted (Fernet) or in the system keyring.'),
            ('Process to analysis-ready', 'Atmospheric correction (DOS, Sen2Cor, 6S), cloud masking and filling, reprojection, pan-sharpening, mosaicking, 17 spectral indices, and SAR calibration and despeckling.'),
            ('Publish cloud-native', 'Cloud Optimized GeoTIFF, GeoParquet, FlatGeobuf and PMTiles; raster2pm converts very large GeoTIFFs to PMTiles block by block.'),
            ('Automate and guard quality', 'YAML pipelines with scheduling and run history; geo-repair and pygeoproof for validation and drift detection; pytest on GitHub Actions with Codecov coverage.'),
        ],
        evidence=[('22', 'Verified data providers behind one API'), ('17', 'Spectral indices built in'),
                  ('64 GB', 'Orthomosaic converted to PMTiles with raster2pm'), ('200+', 'Tests in the geoviz toolkit')],
        evidence_note='pygeofetch is published on PyPI, CI-tested, documented on Read the Docs and archived on Zenodo (doi:10.5281/zenodo.22087230).',
        projects=['mexico-city-subsidence', 'obuasi-ndvi-trend'],
        tools=['pygeofetch', 'STAC 1.0', 'COG', 'GeoParquet', 'FlatGeobuf', 'PMTiles', 'OGC WMS / WFS / WCS', 'GDAL / OGR', 'Rasterio', 'Xarray', 'raster2pm', 'GitHub Actions'],
        different=[
            ('Provider-agnostic by design', 'Switch between Copernicus, USGS, NASA or commercial imagery without rewriting the pipeline.'),
            ('Verified, not just downloaded', 'Checksums, resumable transfers and a doctor command for install and connectivity diagnostics.'),
            ('Production habits from day one', 'Typed APIs, test suites, CI coverage and documentation, as in any software product.'),
        ],
        faq=[
            ('Can it work with commercial imagery?', 'Yes. Planet and Maxar are among the supported providers, alongside the public archives; you supply your own credentials.'),
            ('Will it run on our infrastructure?', 'The tools are Python packages with Docker support, so they run on a laptop, a server or cloud instances such as AWS EC2.'),
            ('Do we get the code?', 'Yes. Pipelines are delivered as code and configuration built on open-source packages, so your team can maintain and extend them.'),
        ],
    ),
    dict(
        slug='backend-cloud', icon='ICON_CLOUD', img='image-61',
        title='Backend & Cloud',
        tagline='Geospatial products people can use — APIs, alerts and dashboards in production.',
        lead=('Analysis only matters when it reaches the person who has to act. I build the Django, FastAPI and PostGIS backends, '
              'real-time feeds and alerting that turn EO and sensor data into working services, and I deploy them reproducibly.'),
        deliver=[
            'Spatial REST and WebSocket APIs on Django or FastAPI with PostgreSQL / PostGIS',
            'IoT ingestion over MQTT and scheduled satellite processing with Celery',
            'Alerting through WhatsApp and SMS, PDF reporting and live dashboards',
            'QGIS plugins that bring your service into analysts\' existing tools',
            'Dockerised deployments on AWS, with automated tests and CI',
        ],
        audience=[
            ('Early-warning programmes', 'Flood, hazard or crop alerts that must reach communities quickly.'),
            ('Energy & infrastructure developers', 'Fast, explainable screening of candidate sites.'),
            ('Start-ups & product teams', 'Location-aware products that need a solid spatial backend and API.'),
            ('Research teams', 'Turning a working notebook into a service others can use.'),
        ],
        approach=[
            ('Model the domain spatially first', 'Design the PostGIS schema around the real-world entities, such as gauges, catchments, sites and constraint layers, so every output traces back to its data.'),
            ('Design for the latency the decision needs', 'Site screening was designed for sub-500 ms assessments, using Redis and spatially indexed layers; batch jobs run on Celery schedules.'),
            ('Ingest real-world data robustly', 'MQTT from ESP32 sensors, scheduled Sentinel-1 / 2 processing and validated inputs, so the service keeps running when one feed fails.'),
            ('Deliver where users already are', 'WhatsApp and SMS alerts, QGIS plugins, PDF reports and live WebSocket dashboards rather than another login.'),
            ('Ship in phases, with tests', 'Flood Watch shipped in five delivery phases, each with its own automated tests, so new features do not break earlier ones.'),
            ('Deploy reproducibly', 'Docker and AWS (EC2, S3), with GitHub Actions CI and split settings for each environment.'),
        ],
        evidence=[('10', 'PostGIS spatial data models behind Flood Watch Ghana'), ('< 500 ms', 'Site-screening design target across 15 layers'),
                  ('5', 'Tested delivery phases for Flood Watch Ghana'), ('AWS', 'Certified Solutions Architect – Professional')],
        evidence_note='Flood Watch Ghana combines MQTT sensor ingestion, Celery-scheduled Sentinel-1 / 2 flood detection and Twilio WhatsApp / SMS alerts; Fatal Flaw delivers PDF reports and a QGIS plugin from one FastAPI service.',
        projects=['flood-watch-ghana', 'fatal-flaw-risk-platform', 'urban-subsidence-watcher'],
        tools=['Django', 'FastAPI', 'PostgreSQL / PostGIS', 'Redis', 'Celery', 'MQTT', 'WebSockets', 'Docker', 'AWS EC2 / S3', 'GitHub Actions'],
        different=[
            ('Geospatial-native backends', 'PostGIS sits at the core, not as an afterthought, so spatial queries are fast and correct.'),
            ('Built for real conditions', 'Low-bandwidth delivery channels, intermittent sensors and users without GIS training.'),
            ('Cloud-certified', 'AWS Certified Solutions Architect – Professional, with production deployments to match.'),
        ],
        faq=[
            ('Do you build the front end too?', 'I focus on backends, APIs and data, and build dashboards and server-rendered interfaces (for example Django with HTMX). For complex single-page front ends I can pair with a front-end specialist.'),
            ('Where will it be hosted?', 'Wherever suits you: AWS or your own servers. Everything is containerised with Docker.'),
            ('Can you integrate with our existing GIS?', 'Yes. Services expose standard APIs and formats, and a QGIS plugin can bring results directly into analysts\' projects.'),
        ],
    ),
    dict(
        slug='applied-eo-research', icon='ICON_LEAF', img='p-croptype-lg',
        title='Applied EO Research',
        tagline='Digital twins and monitoring for agriculture, forests and coasts.',
        lead=('I apply Earth observation to concrete environmental questions: what is growing where, how vegetation responds to '
              'rainfall, where forest carbon is heading and how fast a coastline is retreating. Every answer is fused from '
              'several sensors and validated before it is reported.'),
        deliver=[
            'Crop-type and crop-condition maps at 10 m',
            'Field-level vegetation forecasts driven by rainfall and soil moisture',
            'Forest biomass and carbon forecasts under climate scenarios for REDD+',
            'Shoreline-change forecasts with uncertainty',
            'Land-degradation and mining-impact assessments with clear, quotable figures',
            'Reproducible notebooks and technical reports',
        ],
        audience=[
            ('Agricultural programmes & supply chains', 'Including cocoa and smallholder systems in West Africa.'),
            ('Forest-carbon & REDD+ projects', 'Needing biomass trends and forward-looking scenarios.'),
            ('Coastal authorities', 'Monitoring erosion hotspots before infrastructure is lost.'),
            ('NGOs proving impact', 'Monitoring land and forests with satellite data and participatory ground truth.'),
        ],
        approach=[
            ('Frame the environmental indicator', 'Agree what is measured (NDVI trend, crop type, biomass, shoreline position), at what scale and for which decision.'),
            ('Fuse complementary sources', 'Sentinel-1 and -2, Landsat, GEDI LiDAR, SMAP, ERA5, CHIRPS, ESA CCI soil moisture and UAV orthomosaics, each covering another\'s blind spots.'),
            ('Ground it in the field', 'Participatory plot-level ground truth, UAV-derived labels and DSAS transects anchor the models to reality.'),
            ('Model change over time', 'LSTMs, Bayesian LSTMs and temporal graph neural networks capture lagged responses and trends; scenario runs extend them under RCP pathways.'),
            ('Validate spatially and quantify uncertainty', 'Spatial-block cross-validation and held-out areas, with uncertainty reported alongside every forecast.'),
            ('Translate into decisions', 'Clear figures and hotspot maps, such as "32.0% of the district in measurable decline", that stakeholders can use directly.'),
        ],
        evidence=[('32.0%', 'Of Obuasi district in measurable vegetation decline (2018–2024)'), ('R² > 0.50', 'Parcel-level NDVI forecasts, MAE below 0.07'),
                  ('< 8 m', 'MAE for 3-month shoreline forecasts'), ('333.9 km²', 'Under automated change detection for Rainforest Alliance')],
        evidence_note='Figures come from the Obuasi, Agricultural Digital Twin and Coastal Erosion projects and from Rainforest Alliance work in 2024.',
        projects=['agricultural-digital-twin', 'smart-forest', 'coastal-erosion-digital-twin', 'obuasi-ndvi-trend'],
        tools=['Sentinel-1 / 2', 'Landsat', 'GEDI', 'SMAP', 'ERA5', 'CHIRPS', 'ESA CCI', 'Google Earth Engine', 'LSTM', 'Temporal GNNs', 'DSAS'],
        different=[
            ('Multi-sensor by default', 'Radar, optical, LiDAR and climate data together, rather than a single index.'),
            ('Local landscapes, real examples', 'Built on West African systems such as cocoa farms, the Atewa range and Lake Volta shorelines.'),
            ('Forecasts with error bars', 'Forward-looking products always carry their uncertainty.'),
        ],
        faq=[
            ('Can you work in data-poor regions?', 'Yes. Most of my work is in Ghana, where cloud cover and sparse labels are normal. Radar, open datasets and participatory ground truth fill the gaps.'),
            ('How accurate will the maps be?', 'That is measured, not promised. Accuracy is reported from spatial cross-validation and field checks, so the figure reflects new areas rather than the training data.'),
            ('Do you publish the methods?', 'Wherever possible, yes, as reproducible notebooks built on open-source tools.'),
        ],
    ),
    dict(
        slug='field-validation', icon='ICON_FIELD', img='p-road-lg',
        title='Field Survey & Validation',
        tagline='Ground truth that makes remote sensing trustworthy.',
        lead=('A satellite product is only as credible as its validation. Trained as a geomatic engineer, I design and carry out '
              'the GNSS, Total Station and UAV surveys that calibrate and test Earth observation models, and I report accuracy '
              'in terms decision-makers understand.'),
        deliver=[
            'Validation campaign design: what to measure, where and how many samples',
            'GNSS and Total Station ground-control networks',
            'UAV photogrammetry, orthomosaics and labels for model training',
            'Participatory plot-level ground-truth protocols',
            'Accuracy assessments comparing EO outputs with field measurements',
        ],
        audience=[
            ('EO and AI projects', 'That need independent evidence that their maps are right.'),
            ('Mining & infrastructure', 'Survey control for validating satellite- and drone-derived models.'),
            ('Transport agencies', 'Metric-accurate road assessment from low-cost sensors.'),
            ('Research teams', 'Designing validation that will stand up to peer review.'),
        ],
        approach=[
            ('Design validation before collecting data', 'Choose the error metric and a sampling design stratified across conditions, so validation is not biased toward easy areas.'),
            ('Establish survey control', 'GNSS receivers and Total Stations set ground-control points that tie everything to a known reference.'),
            ('Capture at the right scale', 'UAV flights provide high-resolution orthomosaics and labels where satellite resolution is not enough.'),
            ('Involve local knowledge', 'Participatory plot-level ground truth brings in what only people on the land know.'),
            ('Compare like with like', 'Co-register field and EO data carefully; the TRECK road study compared outputs with 50 surveyed measurements along 50 km.'),
            ('Report accuracy honestly', 'State errors, coverage and known gaps, so users know where a product can be relied on.'),
        ],
        evidence=[('50 / 50 km', 'Surveyed ground-truth measurements / road length (TRECK)'), ('333.9 km²', 'Monitored with participatory ground truth'),
                  ('First Class', 'BSc Geomatic Engineering, KNUST'), ('88%', 'Best Final Year Project, sensor fusion & computer vision')],
        evidence_note='Field experience includes establishing ground-control points with Total Stations, GNSS and UAVs at Asanko Gold Ghana (2023).',
        projects=['treck-road-assessment', 'uav-cocoa-counting', 'atewa-mining-detector'],
        tools=['GNSS', 'Total Station', 'UAV photogrammetry', 'Ground-control networks', 'Sensor fusion (camera / IMU / GPS)', 'QGIS', 'ArcGIS Pro'],
        different=[
            ('Engineer and data scientist', 'I understand both the survey instrument and the model it validates.'),
            ('Validation designed in', 'Sampling and metrics are planned at the start of a project, not after the map is finished.'),
            ('Metric accuracy', 'Results expressed in real-world units, such as metres, centimetres and counts, rather than abstract scores alone.'),
        ],
        faq=[
            ('Can you validate a product someone else built?', 'Yes. Independent validation is often the most credible kind; I design the sampling and comparison around your product and its intended use.'),
            ('Do you need to be on site?', 'For GNSS, Total Station and UAV work, yes, or a local team can follow a protocol I design. Analysis and reporting can be remote.'),
            ('What does an accuracy report contain?', 'The sampling design, error metrics with confidence, maps of where errors occur, and recommendations on where the product should not be used.'),
        ],
    ),
]
