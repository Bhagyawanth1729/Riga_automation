"""Full domain registry for Project Riga (from Domain Reference documentation).

Structure: subject -> domain -> list of subdomains.
Used by the validator and interactive CLI.
"""

BIOLOGY_DOMAINS = {
    "Cell Biology": [
        "Cell structure and organelles", "Membrane structure and transport",
        "Cell cycle and mitosis", "Meiosis and gametogenesis",
        "Cytoskeleton and cell motility", "Cell communication",
        "Cell differentiation and specialization", "Cell death and survival",
    ],
    "Molecular Biology": [
        "DNA structure and replication", "Transcription", "RNA processing",
        "Translation", "Gene regulation", "Mutations and molecular consequences",
        "Molecular techniques", "Genome editing",
    ],
    "Genetics and Genomics": [
        "Mendelian inheritance", "Non-Mendelian inheritance", "Pedigree analysis",
        "Linkage and recombination", "Chromosomal abnormalities",
        "Quantitative genetics", "Genomics", "Population genetics",
    ],
    "Evolutionary Biology": [
        "Natural selection", "Genetic drift and gene flow", "Mutation and variation",
        "Phylogenetics", "Speciation", "Evolutionary mechanisms",
        "Molecular evolution", "Adaptation and life-history evolution",
    ],
    "Ecology": [
        "Population ecology", "Community ecology", "Ecosystem ecology",
        "Behavioral ecology", "Conservation biology", "Biogeography",
        "Ecological modeling", "Human impacts and global change",
    ],
    "Physiology and Homeostasis": [
        "Homeostasis and feedback", "Cardiovascular physiology",
        "Respiratory physiology", "Renal and osmoregulatory physiology",
        "Digestive physiology and nutrition", "Endocrine physiology",
        "Musculoskeletal physiology", "Thermoregulation and stress physiology",
    ],
    "Anatomy and Morphology": [
        "Human anatomy", "Comparative anatomy", "Tissue structure",
        "Organ systems", "Morphological traits", "Plant anatomy",
        "Developmental morphology", "Anatomical imaging and diagrams",
    ],
    "Developmental Biology": [
        "Gametogenesis and fertilization", "Cleavage and gastrulation",
        "Organogenesis", "Cell fate and differentiation", "Pattern formation",
        "Developmental gene regulation", "Stem cells and regeneration",
        "Developmental disorders",
    ],
    "Microbiology and Virology": [
        "Bacterial cell structure", "Microbial growth", "Microbial metabolism",
        "Microbial genetics", "Virology", "Pathogenesis and virulence",
        "Antimicrobials and resistance", "Microbial ecology",
    ],
    "Immunology": [
        "Innate immunity", "Adaptive immunity", "Antibodies and antigens",
        "Major histocompatibility complex", "Vaccination and immunological memory",
        "Hypersensitivity and autoimmunity", "Immunodeficiency",
        "Immunological assays",
    ],
    "Neuroscience and Behavior": [
        "Neuron structure and function", "Membrane potentials and action potentials",
        "Synaptic transmission", "Sensory systems", "Motor systems",
        "Brain regions and circuits", "Learning and plasticity", "Behavioral biology",
    ],
    "Plant Biology": [
        "Plant cells and tissues", "Photosynthesis",
        "Plant water and nutrient transport", "Plant growth and hormones",
        "Plant reproduction", "Plant responses to environment",
        "Plant diversity and classification", "Plant biotechnology",
    ],
    "Biochemistry and Metabolism": [
        "Biomolecules", "Protein structure and function", "Enzyme kinetics",
        "Cellular respiration", "Fermentation and anaerobic metabolism",
        "Photosynthetic metabolism", "Metabolic regulation", "Bioenergetics",
    ],
    "Bioinformatics and Computational Biology": [
        "Sequence alignment", "Genome annotation", "Phylogenomic analysis",
        "Transcriptomics", "Proteomics", "Biological databases and identifiers",
        "Network biology", "Computational modeling",
    ],
    "Experimental Biology and Biostatistics": [
        "Experimental design", "Microscopy and imaging", "Laboratory assays",
        "Data visualization", "Biostatistical inference",
        "Experimental controls and validity", "Dose-response and response curves",
        "Measurement error and uncertainty",
    ],
    "Taxonomy and Biodiversity": [
        "Biological classification", "Species concepts", "Prokaryotic diversity",
        "Protist and fungal diversity", "Animal diversity", "Plant diversity",
        "Biodiversity metrics", "Identification keys and diagnostic traits",
    ],
}

CHEMISTRY_DOMAINS = {
    "Physical Chemistry": [
        "Thermodynamics", "Kinetics", "Quantum chemistry", "Spectroscopy",
        "Statistical mechanics", "Electrochemistry", "Surface chemistry",
        "Photochemistry", "Nernst equation",
    ],
    "Organic Chemistry": [
        "Synthesis and retrosynthesis", "Reaction mechanisms", "Stereochemistry",
        "Named reactions", "Protecting groups", "Asymmetric synthesis",
        "Physical organic chemistry", "Pericyclic reactions",
    ],
    "Inorganic Chemistry": [
        "Coordination chemistry", "Organometallic chemistry", "Main group chemistry",
        "Transition metal chemistry", "Bioinorganic chemistry", "Solid state chemistry",
        "Crystal field theory", "Symmetry and group theory",
    ],
    "Analytical Chemistry": [
        "Spectroscopic analysis", "Chromatography", "Mass spectrometry",
        "Electrochemical analysis", "Titrations", "Quality control",
        "Trace analysis", "Separation science",
    ],
    "Biochemistry": [
        "Enzyme mechanisms", "Metabolic pathways", "Bioenergetics",
        "Protein chemistry", "Nucleic acid chemistry", "Lipid chemistry",
        "Membrane biochemistry", "Signal transduction chemistry",
    ],
    "Materials Chemistry": [
        "Polymers", "Nanomaterials", "Metal-organic frameworks",
        "Semiconductors", "Ceramics", "Composites", "Thin films", "Catalysts",
    ],
    "Computational Chemistry": [
        "DFT methods", "Molecular dynamics", "Ab initio methods",
        "Basis sets", "Force fields", "Reaction path sampling",
    ],
    "Electrochemistry": [
        "Nernst equation", "Electrode kinetics", "Corrosion",
        "Batteries and fuel cells", "Electroanalysis", "Electrosynthesis",
    ],
    "Photochemistry": [
        "Excited states", "Quantum yields", "Photochemical reactions",
        "Solar energy conversion", "Photodynamic therapy",
    ],
    "Spectroscopy": [
        "NMR", "IR and Raman", "UV-Vis", "Mass spectrometry",
        "X-ray spectroscopy", "EPR/ESR", "Circular dichroism",
    ],
}

PHYSICS_DOMAINS = {
    "Classical Mechanics": [
        "Newtonian dynamics", "Lagrangian mechanics", "Hamiltonian mechanics",
        "Central forces and orbits", "Rigid body dynamics", "Oscillations and waves",
        "Chaos and nonlinear dynamics", "Continuum mechanics",
    ],
    "Electromagnetism": [
        "Electrostatics", "Magnetostatics", "Maxwell's equations",
        "Electromagnetic waves", "Waveguides and transmission lines",
        "Radiation", "Circuits", "Boundary value problems",
    ],
    "Quantum Mechanics": [
        "Perturbation theory", "Identical particles", "Angular momentum and spin",
        "Scattering theory", "Hydrogen atom", "Harmonic oscillator",
        "Approximation methods", "Quantum information", "Quantum optics",
    ],
    "Statistical Physics": [
        "Ensemble theory", "Classical statistics", "Quantum statistics",
        "Phase transitions", "Fluctuations", "Kinetic theory",
        "Non-equilibrium statistical mechanics", "Critical phenomena",
    ],
    "Thermodynamics": [
        "Laws of thermodynamics", "Thermodynamic potentials",
        "Heat engines and entropy", "Phase equilibria", "Maxwell relations",
    ],
    "Relativity": [
        "Special relativity", "General relativity", "Relativistic kinematics",
        "Spacetime and metrics", "Relativistic electrodynamics",
    ],
    "Optics": [
        "Geometrical optics", "Physical optics", "Interference and diffraction",
        "Polarization", "Laser physics", "Quantum optics", "Nonlinear optics",
    ],
    "Condensed Matter": [
        "Electronic band structure", "Phonons", "Superconductivity",
        "Magnetism", "Semiconductors", "Topological matter", "Transport phenomena",
    ],
    "Particle Physics": [
        "Standard Model", "Decay kinematics", "Collider physics",
        "Symmetries and conservation laws", "Neutrino physics",
    ],
    "Nuclear Physics": [
        "Nuclear structure", "Radioactive decay", "Nuclear reactions",
        "Fission and fusion", "Shell model",
    ],
    "Astrophysics": [
        "Stellar structure", "Orbital dynamics and binary systems",
        "Cosmology", "Compact objects", "Radiative transfer",
    ],
    "Fluid Dynamics": [
        "Navier-Stokes equations", "Boundary layers", "Turbulence",
        "Compressible flow", "Hydrodynamic stability",
    ],
    "Biophysics": [
        "Polymer physics", "Membrane biophysics", "Single-molecule biophysics",
        "Fluctuation theorems", "Stochastic processes in biology",
    ],
}

DOMAIN_REGISTRY = {
    "biology": BIOLOGY_DOMAINS,
    "chemistry": CHEMISTRY_DOMAINS,
    "physics": PHYSICS_DOMAINS,
}
