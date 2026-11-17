"""Content for the ePortfolio page (Copernicus Master in Digital Earth).

Edit freely, then run:  python3 src/build.py
The learning-journey text is a first draft: rewrite it in your own words.

To add a course, append to COURSES, e.g.
    dict(code='Semester 1', title='Advanced Remote Sensing', ects='5',
         what='What the course covered, in one or two sentences.',
         work='What you produced: assignment, project, poster or code.',
         link='https://github.com/...',          # optional, '' for none
         learned='One or two sentences on what you took away from it.'),
"""

EPORTFOLIO = dict(
    title='ePortfolio',
    tagline='Copernicus Master in Digital Earth: what I study, what I make and where I am heading.',
    img='image-61',
    intro=('This is my ePortfolio for the Copernicus Master in Digital Earth, an Erasmus Mundus joint Master\'s degree. '
           'It records the courses I take, the work I produce in them and what I learn along the way, and it shows where '
           'this programme fits in my path from geomatic engineering in Ghana to radar remote sensing and AI. '
           'I update it as each module finishes.'),
    programme=[
        ('Year 1 · University of Salzburg (PLUS), Austria',
         'Since September 2026. Earth observation, geospatial data science and machine learning for satellite data. '
         'Alongside my studies I work as a student assistant at the Department of Geoinformatics (Z_GIS) in '
         'Prof. Dr. Thomas Blaschke\'s group, in the new GeoInnovation:Lab.'),
        ('Year 2 · University of South Brittany (UBS), France',
         'From autumn 2027, specialising in Artificial Intelligence for Earth Observation (AI4EO), with my Master\'s '
         'thesis in the second year.'),
    ],
    trajectory=[
        ('Geomatic engineering at KNUST (2020–2024)',
         'Surveying, geodesy, photogrammetry and remote sensing in Kumasi, Ghana. I graduated with First Class Honours; '
         'my final-year project on sensor fusion and computer vision was the best in the department. I continued that work as '
         'principal researcher on a camera, IMU and GPS road-assessment system at the Roadessy Lab (TRECK).'),
        ('Field and industry work in Ghana (2023–2026)',
         'Mine surveying with GNSS, total stations and drones; spatial databases and map tiles; change detection for the '
         'Rainforest Alliance; and AI for agriculture, where a crop-disease model that looked excellent in testing failed '
         'on smallholder farms. That failure taught me to validate models in places they have never seen.'),
        ('Building open tools (2025 onwards)',
         'I started writing the software I kept missing: pygeofetch for finding, downloading and processing satellite data, '
         'and pygeovision for running AI models from an area of interest to a finished map. Through EOCoreINT I share these '
         'tools and teach remote sensing to students and young professionals in Africa.'),
        ('Turning to radar (2025 onwards)',
         'Radar sees through the clouds that block optical satellites over West Africa for much of the year. I built a full '
         'Sentinel-1 InSAR chain, tested it on Mexico City\'s subsidence, and began research on learned phase unwrapping '
         '(pyunwrap) and graph neural networks for persistent scatterers (ps-gnn).'),
        ('Salzburg (2026 onwards)',
         'The Copernicus Master and my work at Z_GIS brought this together. In Prof. Blaschke\'s group I work on geospatial '
         'compliance and mining monitoring, with a planned link to the spin-off PeaceEye and future work in Ghana. With colleagues '
         'there I am developing PhysInSAR, which estimates ground motion from Sentinel-1 and NISAR together, and preparing my first journal papers.'),
    ],
    journey=[
        'The biggest change since I arrived in Salzburg is how I judge my own work. Before, a model or a map was finished when '
        'it ran. Now I ask what would prove it wrong, and I build that test first: simulated data with known answers, held-out '
        'data, comparison with GNSS stations. Some of my most useful results came from these checks failing, like the Mexico City '
        'network that split into 17 parts, or a model whose training labels turned out not to measure what I cared about.',
        'I have also learned to work as part of a research group: writing papers with co-authors, agreeing what to share and when, '
        'and taking feedback on drafts. Studying in Europe as a student from Ghana has not always been easy, but it has made '
        'me more focused on the work that matters most to me.',
    ],
    next=[
        ('Publish', 'Submit my research papers on learned InSAR unwrapping, persistent-scatterer selection and PhysInSAR, and the '
                    'software papers on pygeofetch and pygeovision, during 2027.'),
        ('Gain industry experience', 'Spend summer 2027 in a SAR or Earth observation internship, working on real data at scale.'),
        ('Specialise in AI4EO', 'Join the AI for Earth Observation specialisation at UBS in autumn 2027 and write my Master\'s thesis '
                                'on multi-frequency radar interferometry.'),
        ('Longer term', 'A PhD or research-engineering role in radar remote sensing, and bringing these methods back to monitoring '
                        'mining, land and ground motion in West Africa.'),
    ],
    evidence=['mexico-city-subsidence', 'pyunwrap', 'ps-gnn', 'atewa-mining-detector', 'treck-road-assessment', 'obuasi-ndvi-trend'],
    skills=['Sentinel-1 InSAR', 'NISAR', 'SBAS', 'Phase unwrapping', 'PyTorch', 'Graph neural networks', 'EO foundation models',
            'Model evaluation', 'STAC / COG', 'Python packaging', 'Spatial databases', 'Agent-based modelling', 'Scientific writing', 'Teaching', 'German (A1, in progress)'],
)

SEMESTER = 'Winter semester 2026/27 · University of Salzburg'

# group: theme heading on the page. work / learned / link: fill in as each course finishes ('' hides the line).
COURSES = [
    # Earth observation and image analysis
    dict(group='Earth observation and image analysis', code='856.231', title='Advanced Remote Sensing', ects='6',
         what='The full image-analysis workflow, from new sensors (hyperspectral, radar, LiDAR, drones) through radiometric correction, '
              'filtering and segmentation to CNNs, random forests, SVMs, knowledge-based classification and validation.',
         work='', learned='', link=''),
    dict(group='Earth observation and image analysis', code='856.288', title='Object-based Image Analysis', ects='3',
         what='Image segmentation, hierarchy and knowledge representation, object-based classification and class modelling, '
              'and accuracy assessment for very-high-resolution and Sentinel-2 imagery.',
         work='', learned='', link=''),
    dict(group='Earth observation and image analysis', code='856.285', title='Digital Earth: Big Earth Data Concepts', ects='3',
         what='Accessing and processing very large Earth observation archives: data cubes, knowledge-based systems and machine '
              'learning for continental- and global-scale analysis.',
         work='', learned='', link=''),
    dict(group='Earth observation and image analysis', code='651.010', title='Copernicus in Digital Earth (EO*GI)', ects='1',
         what='How the Copernicus programme is built, from satellites and ground segment to its information services, and how to '
              'judge the quality of global geospatial datasets.',
         work='', learned='', link=''),
    # Data, software and modelling
    dict(group='Data, software and modelling', code='651.051', title='Practice: Software Development', ects='3',
         what='Software engineering for geoinformatics: programming styles, version control and project management, GDAL, rasterio, '
              'QGIS and the OpenStreetMap API, ending in a group project on GitHub or GitLab.',
         work='', learned='', link=''),
    dict(group='Data, software and modelling', code='856.286', title='Spatio-temporal Data Analytics', ects='3',
         what='Relational and spatial databases with PostgreSQL/PostGIS and QGIS: SQL, spatial operations, integrity and '
              'optimisation, with a look at NoSQL and in-memory systems.',
         work='', learned='', link=''),
    dict(group='Data, software and modelling', code='856.261', title='Design of Geospatial Data Models and Services', ects='3',
         what='Standardised geospatial data models as used in INSPIRE: UML, the General Feature Model, XML and GML.',
         work='', learned='', link=''),
    dict(group='Data, software and modelling', code='856.284', title='Spatial Simulation', ects='6',
         what='Cellular automata and agent-based models on real geodata in GAMA, with AI-assisted coding where the modeller stays '
              'in charge: designing the model, checking the code and telling emergence from bugs.',
         work='', learned='', link=''),
    dict(group='Data, software and modelling', code='651.011', title='Spatial Thinking & Modelling', ects='2',
         what='Spatial concepts and models, from location, distance and shape to spatial behaviour, and training in spatial '
              'orientation and visualisation.',
         work='', learned='', link=''),
    # Applications and professional development
    dict(group='Applications and professional development', code='856.114', title='GeoHumanitarian Action', ects='4',
         what='Earth observation and GIS in humanitarian work: key actors, population and building-footprint data, flood and fire '
              'mapping, and two simulated disaster sprints in small teams.',
         work='', learned='', link=''),
    dict(group='Applications and professional development', code='651.012', title='Career Development & ePortfolio', ects='1',
         what='Careers in Earth observation and geoinformatics, start-ups, a personal SWOT analysis, internship applications and '
              'this ePortfolio.',
         work='', learned='', link=''),
    dict(group='Applications and professional development', code='651.990', title='German language course (A1)', ects='2',
         what='Basic German grammar and vocabulary for everyday situations, towards level A1.',
         work='', learned='', link=''),
]
