"""Topic dependency graph for the precision agriculture book.

Maps concepts to chapters and defines prerequisite relationships
so the system can guide students through topics in order.
"""

from dataclasses import dataclass, field


@dataclass
class Concept:
    """A concept/topic in the book."""
    name: str
    chapter: int
    section: str = ""
    prerequisites: list[str] = field(default_factory=list)
    description: str = ""


# ---------------------------------------------------------------------------
# The concept graph -- topics and their prerequisites across 20 chapters
# ---------------------------------------------------------------------------
CONCEPT_GRAPH: dict[str, Concept] = {

    # ===== Chapter 1: Why Precision Agriculture? =====
    "global_food_challenge": Concept(
        "Global Food Challenge", 1, "1.1",
        [],
        "Population growth, land constraints, and the environmental cost of uniform farming",
    ),
    "what_is_precision_agriculture": Concept(
        "What Is Precision Agriculture", 1, "1.3",
        ["global_food_challenge"],
        "Definition, core principles: right input, right place, right time, right amount",
    ),
    "pa_cycle": Concept(
        "The PA Cycle: Sense-Analyze-Act", 1, "1.4",
        ["what_is_precision_agriculture"],
        "Data acquisition, interpretation/decision support, variable-rate implementation",
    ),
    "pa_sustainability": Concept(
        "PA and Environmental Sustainability", 1, "1.5",
        ["what_is_precision_agriculture"],
        "Reduced nutrient runoff, lower pesticide use, carbon management",
    ),

    # ===== Chapter 2: The Agricultural Landscape =====
    "why_fields_vary": Concept(
        "Why Fields Are Not Uniform", 2, "2.1",
        [],
        "Natural and human-induced causes of within-field variability",
    ),
    "soil_basics": Concept(
        "Soil Fundamentals", 2, "2.2",
        ["why_fields_vary"],
        "Texture, structure, organic matter, pH, cation exchange capacity",
    ),
    "topography_effects": Concept(
        "Topography and Crop Production", 2, "2.3",
        ["why_fields_vary"],
        "Water redistribution, erosion, aspect, DEMs in agriculture",
    ),
    "microclimate_variability": Concept(
        "Climate and Microclimate Variability", 2, "2.4",
        ["why_fields_vary"],
        "Regional climate, weather year-to-year variability, field-scale microclimates",
    ),

    # ===== Chapter 3: The Data Revolution in Farming =====
    "data_driven_farming": Concept(
        "Data-Driven Decision Making", 3, "3.1",
        ["what_is_precision_agriculture"],
        "Transition from intuition to data-driven farm management",
    ),
    "agricultural_data_types": Concept(
        "Types of Agricultural Data", 3, "3.2",
        ["data_driven_farming"],
        "Spatial, temporal, spectral, and tabular data in agriculture",
    ),
    "gis_in_agriculture": Concept(
        "GIS in Agriculture", 3, "3.3",
        ["agricultural_data_types"],
        "What GIS does, spatial analysis functions, software platforms",
    ),
    "iot_on_farm": Concept(
        "Internet of Things on the Farm", 3, "3.4",
        ["data_driven_farming"],
        "Sensor networks, connectivity, monitoring-to-automation pipeline",
    ),

    # ===== Chapter 4: Satellite and Aerial Remote Sensing =====
    "electromagnetic_spectrum": Concept(
        "Electromagnetic Spectrum and Plant Interactions", 4, "4.1",
        [],
        "How plants absorb, reflect, and transmit radiation across wavelengths",
    ),
    "satellite_platforms": Concept(
        "Satellite Platforms for Agriculture", 4, "4.2",
        ["electromagnetic_spectrum"],
        "Landsat, Sentinel, Planet, commercial high-res satellites",
    ),
    "drones_in_agriculture": Concept(
        "Drones (UAVs) in Agriculture", 4, "4.3",
        ["electromagnetic_spectrum"],
        "Fixed-wing and multirotor, sensor payloads, regulatory aspects",
    ),
    "ndvi": Concept(
        "NDVI and Vegetation Indices", 4, "4.4",
        ["electromagnetic_spectrum"],
        "Normalized Difference Vegetation Index, EVI, and other indices",
    ),

    # ===== Chapter 5: Hyperspectral and Multispectral Imaging =====
    "multispectral_vs_hyperspectral": Concept(
        "Multispectral vs. Hyperspectral Imaging", 5, "5.2",
        ["electromagnetic_spectrum"],
        "Band count, spectral resolution, trade-offs between the two",
    ),
    "spectral_signatures": Concept(
        "Spectral Signatures of Crops and Soils", 5, "5.3",
        ["multispectral_vs_hyperspectral"],
        "Spectral libraries, crop fingerprints, soil reflectance patterns",
    ),
    "chlorophyll_nitrogen_estimation": Concept(
        "Chlorophyll, Nitrogen, and LAI Estimation", 5, "5.5",
        ["spectral_signatures", "ndvi"],
        "Using spectral data to estimate plant biochemistry and canopy structure",
    ),
    "soil_spectral_estimation": Concept(
        "Soil Property Estimation from Spectra", 5, "5.6",
        ["spectral_signatures"],
        "Estimating nitrogen, moisture, organic matter from spectral reflectance",
    ),

    # ===== Chapter 6: Proximal and In-Field Sensors =====
    "proximal_sensors": Concept(
        "Proximal Sensors: Principles", 6, "6.1",
        ["pa_cycle"],
        "On-ground sensors: active vs passive, modes of deployment",
    ),
    "soil_ec_mapping": Concept(
        "Soil Electrical Conductivity Mapping", 6, "6.2",
        ["proximal_sensors", "soil_basics"],
        "Veris, EM38, DC resistivity, interpreting ECa maps",
    ),
    "on_the_go_soil_sensing": Concept(
        "On-the-Go Soil pH and Nutrient Sensing", 6, "6.3",
        ["proximal_sensors", "soil_basics"],
        "Ion-selective electrodes, NIR sensing of organic matter",
    ),
    "canopy_sensors": Concept(
        "Crop Canopy Sensors", 6, "6.4",
        ["proximal_sensors", "ndvi"],
        "Tractor-mounted NDVI sensors for real-time crop assessment",
    ),

    # ===== Chapter 7: Positioning and Navigation =====
    "gnss_principles": Concept(
        "GNSS Principles", 7, "7.2",
        [],
        "GPS, GLONASS, Galileo, BeiDou: satellite ranging and positioning",
    ),
    "rtk_correction": Concept(
        "Differential Correction and RTK", 7, "7.3",
        ["gnss_principles"],
        "Error sources, DGPS, RTK, PPP, choosing accuracy levels",
    ),
    "auto_steering": Concept(
        "Auto-Steering and Guidance Systems", 7, "7.4",
        ["rtk_correction"],
        "Lightbar to autonomous steering, implement guidance, overlap reduction",
    ),

    # ===== Chapter 8: Understanding Soil Variability =====
    "soil_variability": Concept(
        "Sources of Soil Variability", 8, "8.1",
        ["why_fields_vary", "soil_basics"],
        "Inherent variability, erosion, salinity, management-induced patterns",
    ),
    "soil_sampling_strategies": Concept(
        "Soil Sampling Strategies", 8, "8.2",
        ["soil_variability"],
        "Grid sampling, zone sampling, directed sampling",
    ),
    "geostatistics_kriging": Concept(
        "Geostatistics: Variograms and Kriging", 8, "8.3",
        ["soil_sampling_strategies", "gis_in_agriculture"],
        "Spatial correlation, ordinary kriging, block kriging, validation",
    ),
    "management_zones": Concept(
        "Management Zones", 8, "8.5",
        ["geostatistics_kriging", "soil_ec_mapping"],
        "Delineating zones of similar productivity for site-specific management",
    ),

    # ===== Chapter 9: Water Management and Irrigation =====
    "soil_plant_atmosphere_continuum": Concept(
        "Soil-Plant-Atmosphere Continuum", 9, "9.2",
        ["soil_basics"],
        "Water movement from soil through plant to atmosphere",
    ),
    "evapotranspiration": Concept(
        "Evapotranspiration and Crop Water Requirements", 9, "9.3",
        ["soil_plant_atmosphere_continuum", "microclimate_variability"],
        "FAO Penman-Monteith, crop coefficients, soil water balance",
    ),
    "soil_moisture_sensing": Concept(
        "Soil Moisture Sensing and Monitoring", 9, "9.4",
        ["iot_on_farm", "soil_plant_atmosphere_continuum"],
        "TDR, capacitance, sensor networks, remote sensing of water status",
    ),
    "variable_rate_irrigation": Concept(
        "Variable Rate Irrigation", 9, "9.6",
        ["evapotranspiration", "management_zones", "rtk_correction"],
        "Site-specific water application using VRI center pivots and drip",
    ),

    # ===== Chapter 10: Nutrient Management =====
    "nutrient_variability": Concept(
        "Why Nutrients Vary Across the Field", 10, "10.1",
        ["soil_variability"],
        "Parent material, topography, management history, salinity effects",
    ),
    "essential_plant_nutrients": Concept(
        "Essential Plant Nutrients", 10, "10.2",
        [],
        "Macro and micronutrients: N, P, K, S, Ca, Mg, Fe, Zn, etc.",
    ),
    "soil_testing": Concept(
        "Soil Testing and Nutrient Mapping", 10, "10.3",
        ["soil_sampling_strategies", "geostatistics_kriging"],
        "Grid and zone sampling for nutrients, geostatistical nutrient maps",
    ),
    "nitrogen_management": Concept(
        "Nitrogen Management", 10, "10.4",
        ["essential_plant_nutrients", "canopy_sensors", "chlorophyll_nitrogen_estimation"],
        "Spatial/temporal N variation, sensor-based in-season N, 4R framework",
    ),

    # ===== Chapter 11: Variable Rate Technology =====
    "vrt_concept": Concept(
        "Variable Rate Application Concept", 11, "11.1",
        ["pa_cycle", "management_zones"],
        "The principle of adjusting inputs spatially across the field",
    ),
    "map_vs_sensor_vrt": Concept(
        "Map-Based vs. Sensor-Based VRT", 11, "11.2",
        ["vrt_concept", "canopy_sensors"],
        "Prescription maps vs real-time sensor feedback vs hybrid approaches",
    ),
    "variable_rate_seeding": Concept(
        "Variable Rate Seeding", 11, "11.3",
        ["vrt_concept", "management_zones"],
        "Adjusting seeding rate by zone based on yield potential",
    ),
    "variable_rate_fertilization": Concept(
        "Variable Rate Fertilization", 11, "11.4",
        ["soil_testing", "nitrogen_management", "vrt_concept"],
        "Site-specific P, K, lime, and N application",
    ),
    "prescription_maps": Concept(
        "Building Prescription Maps", 11, "11.7",
        ["management_zones", "gis_in_agriculture", "vrt_concept"],
        "Data sources, zone delineation, converting zones to application rates",
    ),
    "isobus": Concept(
        "ISOBUS and Equipment Controllers", 11, "11.8",
        ["auto_steering", "vrt_concept"],
        "Task controllers, rate controllers, ISOBUS standard for interoperability",
    ),

    # ===== Chapter 12: Crop Health Monitoring and Protection =====
    "weed_detection": Concept(
        "Weed Detection and Site-Specific Management", 12, "12.2",
        ["drones_in_agriculture", "ndvi"],
        "Patchy weed distribution, detection technologies, herbicide savings",
    ),
    "disease_detection": Concept(
        "Disease Detection: Scouting to Sensors", 12, "12.3",
        ["multispectral_vs_hyperspectral", "chlorophyll_nitrogen_estimation"],
        "Spatial patterns of disease, spectral and imaging-based detection",
    ),
    "pest_monitoring": Concept(
        "Pest Monitoring and IPM", 12, "12.4",
        ["data_driven_farming"],
        "Scouting, growing degree days, economic thresholds, integrated pest management",
    ),
    "remote_sensing_crop_stress": Concept(
        "Remote Sensing for Crop Stress", 12, "12.5",
        ["satellite_platforms", "ndvi", "spectral_signatures"],
        "Using vegetation indices to detect stress before visual symptoms appear",
    ),

    # ===== Chapter 13: Yield Monitoring and Mapping =====
    "yield_monitor_principles": Concept(
        "How Yield Monitors Work", 13, "13.2",
        ["gnss_principles"],
        "Mass flow sensors, moisture sensors, GPS, in-cab displays",
    ),
    "yield_data_errors": Concept(
        "Sources of Error in Yield Data", 13, "13.3",
        ["yield_monitor_principles"],
        "Calibration, combine dynamics, header width, GPS errors",
    ),
    "yield_map_processing": Concept(
        "Yield Map Processing and Cleaning", 13, "13.4",
        ["yield_data_errors", "gis_in_agriculture"],
        "Filtering, interpolation, the H-method, standardization",
    ),
    "yield_map_interpretation": Concept(
        "Interpreting Yield Maps", 13, "13.5",
        ["yield_map_processing", "management_zones"],
        "Multi-year patterns, causal analysis, linking to soil and topography",
    ),

    # ===== Chapter 14: Data Pipelines and Management =====
    "data_lifecycle": Concept(
        "Data Lifecycle in Precision Agriculture", 14, "14.1",
        ["agricultural_data_types"],
        "Collection, storage, cleaning, integration, and archiving of farm data",
    ),
    "data_formats_standards": Concept(
        "Data Formats, Protocols, and Standards", 14, "14.2",
        ["data_lifecycle"],
        "Shapefiles, GeoTIFF, ISOXML, AgGateway ADAPT, data interoperability",
    ),
    "fmis": Concept(
        "Farm Management Information Systems", 14, "14.6",
        ["data_lifecycle", "gis_in_agriculture"],
        "Integrated platforms for planning, recording, and analyzing farm operations",
    ),
    "data_privacy_ownership": Concept(
        "Data Sharing, Privacy, and Ownership", 14, "14.7",
        ["data_lifecycle"],
        "Who owns farm data, privacy concerns, open data initiatives",
    ),

    # ===== Chapter 15: AI and Machine Learning in Agriculture =====
    "ml_fundamentals": Concept(
        "Machine Learning Fundamentals", 15, "15.2",
        ["data_driven_farming"],
        "Supervised, unsupervised, and reinforcement learning basics",
    ),
    "deep_learning_computer_vision": Concept(
        "Deep Learning and Computer Vision", 15, "15.3",
        ["ml_fundamentals"],
        "CNNs, RNNs/LSTMs, GANs, computer vision for field imagery",
    ),
    "ai_yield_prediction": Concept(
        "AI for Crop Classification and Yield Prediction", 15, "15.4",
        ["ml_fundamentals", "satellite_platforms", "yield_map_interpretation"],
        "ML models for crop type mapping and pre-harvest yield estimation",
    ),
    "ai_disease_pest_detection": Concept(
        "AI for Disease and Pest Detection", 15, "15.5",
        ["deep_learning_computer_vision", "disease_detection"],
        "Image-based disease ID, pest classification, multi-source integration",
    ),

    # ===== Chapter 16: Decision Support Systems =====
    "dss_architecture": Concept(
        "DSS Architecture", 16, "16.2",
        ["data_lifecycle", "ml_fundamentals"],
        "Data layer, model layer, user interface in decision support systems",
    ),
    "crop_growth_models": Concept(
        "Crop Growth Models as Decision Tools", 16, "16.3",
        ["evapotranspiration", "essential_plant_nutrients"],
        "DSSAT, APSIM, process-based simulation for management scenarios",
    ),
    "on_farm_experimentation": Concept(
        "On-Farm Experimentation and Strip Trials", 16, "16.4",
        ["yield_map_interpretation", "vrt_concept"],
        "Randomized strip trials, analyzing treatment effects at field scale",
    ),
    "risk_uncertainty": Concept(
        "Risk and Uncertainty in Spatial Decisions", 16, "16.5",
        ["geostatistics_kriging", "dss_architecture"],
        "Probability-based management, kriging variance, stochastic optimization",
    ),

    # ===== Chapter 17: Economics of Precision Agriculture =====
    "pa_cost_benefit": Concept(
        "Cost-Benefit Analysis of PA", 17, "17.2",
        ["what_is_precision_agriculture"],
        "Identifying costs and benefits, NPV, IRR, payback period",
    ),
    "pa_roi_evidence": Concept(
        "Return on Investment Evidence", 17, "17.3",
        ["pa_cost_benefit", "variable_rate_fertilization", "auto_steering"],
        "Empirical ROI data for guidance, VRT, and data-intensive technologies",
    ),
    "pa_adoption_barriers": Concept(
        "Adoption Drivers and Barriers", 17, "17.4",
        ["pa_cost_benefit"],
        "Farm size, complexity, connectivity, trust, and skills gaps",
    ),

    # ===== Chapter 18: Precision Livestock and Beyond =====
    "precision_livestock_farming": Concept(
        "Precision Livestock Farming", 18, "18.1",
        ["what_is_precision_agriculture", "iot_on_farm"],
        "Right input, right animal, right time -- PLF principles",
    ),
    "animal_sensors": Concept(
        "Sensors for Animal Monitoring", 18, "18.2",
        ["precision_livestock_farming"],
        "Accelerometers, GPS, RFID, rumen boluses for livestock",
    ),
    "automated_milking": Concept(
        "Automated Milking Systems", 18, "18.7",
        ["animal_sensors"],
        "Robotic milking, individual cow monitoring, data-driven herd management",
    ),

    # ===== Chapter 19: The Future of Precision Agriculture =====
    "agricultural_robotics": Concept(
        "Agricultural Robotics and Autonomous Systems", 19, "19.2",
        ["auto_steering", "deep_learning_computer_vision"],
        "Autonomous tractors, weeding robots, robotic harvesting",
    ),
    "digital_twins_farming": Concept(
        "Digital Twins for Farm Management", 19, "19.3",
        ["crop_growth_models", "iot_on_farm", "fmis"],
        "Virtual farm replicas updated in real time for simulation and prediction",
    ),
    "edge_ai": Concept(
        "Edge AI and On-Machine Intelligence", 19, "19.4",
        ["deep_learning_computer_vision", "isobus"],
        "Running ML models on tractors and drones for real-time decisions",
    ),
    "carbon_markets_pa": Concept(
        "Carbon Markets and Precision Agriculture", 19, "19.7",
        ["pa_sustainability", "variable_rate_fertilization"],
        "MRV for soil carbon, carbon credits, regenerative agriculture",
    ),
    "ethics_data_sovereignty": Concept(
        "Ethics: Data Sovereignty, Labor, Equity", 19, "19.8",
        ["data_privacy_ownership", "pa_adoption_barriers"],
        "Who controls farm data, labor displacement, the digital divide",
    ),

    # ===== Chapter 20: Precision Agriculture in Hungary =====
    "hungarian_agriculture_context": Concept(
        "Hungarian Agriculture: Landscape and Context", 20, "20.1",
        [],
        "Carpathian Basin soils, land structure, historical transition",
    ),
    "pa_adoption_hungary": Concept(
        "PA Adoption in Hungary", 20, "20.2",
        ["hungarian_agriculture_context", "pa_adoption_barriers"],
        "Current state, machinery market, farm size distribution",
    ),
    "hungarian_soil_mapping": Concept(
        "Soil Mapping and Nutrient Management in Hungary", 20, "20.5",
        ["soil_testing", "management_zones", "hungarian_agriculture_context"],
        "Hungarian soil survey traditions, precision nutrient programs",
    ),
    "hungarian_water_challenges": Concept(
        "Water Management Challenges in Hungary", 20, "20.6",
        ["variable_rate_irrigation", "hungarian_agriculture_context"],
        "Drought risk in the Great Plain, irrigation modernization",
    ),
    "hungarian_policy_framework": Concept(
        "Hungarian Policy: CAP and Digital Agriculture", 20, "20.8",
        ["pa_adoption_hungary"],
        "EU Common Agricultural Policy, national subsidies, digital strategy",
    ),
}


def get_prerequisites(concept_key: str) -> list[str]:
    """Get all prerequisite concepts (recursive) for a given concept."""
    visited = set()
    result = []

    def _walk(key: str):
        if key in visited or key not in CONCEPT_GRAPH:
            return
        visited.add(key)
        for prereq in CONCEPT_GRAPH[key].prerequisites:
            _walk(prereq)
            if prereq not in result:
                result.append(prereq)

    _walk(concept_key)
    return result


def get_concepts_for_chapter(chapter: int) -> list[str]:
    """Get all concept keys for a given chapter number."""
    return [k for k, v in CONCEPT_GRAPH.items() if v.chapter == chapter]


def get_concept_tree() -> dict:
    """Return the full concept graph as a serializable dict."""
    return {
        key: {
            "name": c.name,
            "chapter": c.chapter,
            "section": c.section,
            "prerequisites": c.prerequisites,
            "description": c.description,
        }
        for key, c in CONCEPT_GRAPH.items()
    }
