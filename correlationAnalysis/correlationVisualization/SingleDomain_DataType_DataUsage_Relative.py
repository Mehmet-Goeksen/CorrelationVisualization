# imports
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# define functions to get top correlations
#https://stackoverflow.com/questions/17778394/list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas
def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]


def plotHeatmap(domain, amount):
    # load data
    df_researchers = pd.read_csv('/Users/mehmetgoksen/Library/Mobile Documents/com~apple~CloudDocs/Uni/BA/Scripts/correlationAnalysis/correlationVisualization/datadiscovery_researchers.csv')

    # Get users with single domains
    df_single_domain_researchers = df_researchers[["disc_agricul", "disc_artshuman", "disc_astronom", "disc_biochem", "disc_biological", "disc_busin", "disc_chemeng", "disc_chem", "disc_compsci", "disc_decisionsci", "disc_dentist", "disc_earthplanet", "disc_econ", "disc_energy", "disc_engtech", "disc_environ", "disc_healthprof", "disc_immun", "disc_matlsci", "disc_math", "disc_med", "disc_multi", "disc_neuro", "disc_nurs", "disc_pharma", "disc_physics", "disc_psych", "disc_socsci", "disc_vet", "disc_infosci", "disc_other"]]

    df_single_domain_researchers = (df_single_domain_researchers != "0").astype(int)
    df_single_domain_researchers["sum"] = df_single_domain_researchers.sum(axis=1)

    df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==1]
    df_researchers = df_researchers.iloc[df_index.index, :]

    # get domain-subsets
    df_domains = pd.DataFrame()
    df_researchers = df_researchers.rename(columns={"need_obs": "Observational/Empirical", "need_exp": "Experimental Need", "need_sim": "Simulation", "need_deriv": "Derived/Compiled", "need_oth": "Other Needs", "use_nwstdy": "Basis for new study", "use_calb" : "Calibration", "use_bnchmrk" : "Benchmarking", "use_vrfctn" : "Verification", "use_inpt" : "Input", "use_idea": "Generating new ideas", "use_tch": "Teaching", "use_nwprj" : "Prepare new project/proposal", "use_nwmth" : "Experimental Use", "use_trnds" : "Identifying trends/predictions", "use_cmprsn" : "Comparison", "use_smvs" : "Summarizations", "use_intgrtn" : "Integrate with other data", "use_oth" : "Other Uses"})

    # Agriculture
    agriculture = df_researchers.loc[df_researchers['disc_agricul'] == "Agriculture"]
    agriculture = agriculture[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    agriculture = (agriculture != "0").astype(int)
    agriculture["SumOfAnswers"] = agriculture.sum(axis=1)
    agriculture = agriculture.divide(agriculture["SumOfAnswers"], axis=0)
    agriculture["Domain"] = "Agriculture"
    df_domains = pd.concat([df_domains, agriculture])

    # Arts and Humanities
    artshuman = df_researchers.loc[df_researchers['disc_artshuman'] == "Arts and Humanities"]
    artshuman = artshuman[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    artshuman = (artshuman != "0").astype(int)
    artshuman["SumOfAnswers"] = artshuman.sum(axis=1)
    artshuman = artshuman.divide(artshuman["SumOfAnswers"], axis=0)
    artshuman["Domain"] = "Arts and Humanities"
    df_domains = pd.concat([df_domains, artshuman])

    # Astronomy
    astronom = df_researchers.loc[df_researchers['disc_astronom'] == "Astronomy"]
    astronom = astronom[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    astronom = (astronom != "0").astype(int)
    astronom["SumOfAnswers"] = astronom.sum(axis=1)
    astronom = astronom.divide(astronom["SumOfAnswers"], axis=0)
    astronom["Domain"] = "Astronomy"
    df_domains = pd.concat([df_domains, astronom])

    # Biochemistry, Genetics, Molecular Biology
    biochem = df_researchers.loc[df_researchers['disc_biochem'] == "Biochemistry, Genetics, Molecular Biology"]
    biochem = biochem[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    biochem = (biochem != "0").astype(int)
    biochem["SumOfAnswers"] = biochem.sum(axis=1)
    biochem = biochem.divide(biochem["SumOfAnswers"], axis=0)
    biochem["Domain"] = "Biochemistry, Genetics, Molecular Biology"
    df_domains = pd.concat([df_domains, biochem])

    # Biological Sciences
    biological = df_researchers.loc[df_researchers['disc_biological'] == "Biological Sciences"]
    biological = biological[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    biological = (biological != "0").astype(int)
    biological["SumOfAnswers"] = biological.sum(axis=1)
    biological = biological.divide(biological["SumOfAnswers"], axis=0)
    biological["Domain"] = "Biological Sciences"
    df_domains = pd.concat([df_domains, biological])

    # Business
    busin_df = df_researchers.loc[df_researchers['disc_busin'] == "Business"]
    busin_df = busin_df[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    busin_df = (busin_df != "0").astype(int)
    busin_df["SumOfAnswers"] = busin_df.sum(axis=1)
    busin_df = busin_df.divide(busin_df["SumOfAnswers"], axis=0)
    busin_df["Domain"] = "Business"
    df_domains = pd.concat([df_domains, busin_df])

    # Chemical Engineering
    chemeng = df_researchers.loc[df_researchers['disc_chemeng'] == "Chemical Engineering"]
    chemeng = chemeng[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    chemeng = (chemeng != "0").astype(int)
    chemeng["SumOfAnswers"] = chemeng.sum(axis=1)
    chemeng = chemeng.divide(chemeng["SumOfAnswers"], axis=0)
    chemeng["Domain"] = "Chemical Engineering"
    df_domains = pd.concat([df_domains, chemeng])

    # Chemistry
    chem = df_researchers.loc[df_researchers['disc_chem'] == "Chemistry"]
    chem = chem[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    chem = (chem != "0").astype(int)
    chem["SumOfAnswers"] = chem.sum(axis=1)
    chem = chem.divide(chem["SumOfAnswers"], axis=0)
    chem["Domain"] = "Chemistry"
    df_domains = pd.concat([df_domains, chem])

    # Computer Sciences, IT
    compsci = df_researchers.loc[df_researchers['disc_compsci'] == "Computer Sciences, IT"]
    compsci = compsci[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    compsci = (compsci != "0").astype(int)
    compsci["SumOfAnswers"] = compsci.sum(axis=1)
    compsci = compsci.divide(compsci["SumOfAnswers"], axis=0)
    compsci["Domain"] = "Computer Sciences, IT"
    df_domains = pd.concat([df_domains, compsci])

    # Decision Sciences
    decisionsci = df_researchers.loc[df_researchers['disc_decisionsci'] == "Decision Sciences"]
    decisionsci = decisionsci[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    decisionsci = (decisionsci != "0").astype(int)
    decisionsci["SumOfAnswers"] = decisionsci.sum(axis=1)
    decisionsci = decisionsci.divide(decisionsci["SumOfAnswers"], axis=0)
    decisionsci["Domain"] = "Decision Sciences"
    df_domains = pd.concat([df_domains, decisionsci])

    # Dentistry
    dentist = df_researchers.loc[df_researchers['disc_dentist'] == "Dentistry"]
    dentist = dentist[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    dentist = (dentist != "0").astype(int)
    dentist["SumOfAnswers"] = dentist.sum(axis=1)
    dentist = dentist.divide(dentist["SumOfAnswers"], axis=0)
    dentist["Domain"] = "Dentistry"
    df_domains = pd.concat([df_domains, dentist])

    # Earth and Planetary Sciences
    earthplanet = df_researchers.loc[df_researchers['disc_earthplanet'] == "Earth and Planetary Sciences"]
    earthplanet = earthplanet[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    earthplanet = (earthplanet != "0").astype(int)
    earthplanet["SumOfAnswers"] = earthplanet.sum(axis=1)
    earthplanet = earthplanet.divide(earthplanet["SumOfAnswers"], axis=0)
    earthplanet["Domain"] = "Earth and Planetary Sciences"
    df_domains = pd.concat([df_domains, earthplanet])

    # Economics, Econometrics and Finance
    econ = df_researchers.loc[df_researchers['disc_econ'] == "Economics and Finance"]
    econ = econ[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    econ = (econ != "0").astype(int)
    econ["SumOfAnswers"] = econ.sum(axis=1)
    econ = econ.divide(econ["SumOfAnswers"], axis=0)
    econ["Domain"] = "Economics and Finance"
    df_domains = pd.concat([df_domains, econ])

    # Energy
    energy = df_researchers.loc[df_researchers['disc_energy'] == "Energy"]
    energy = energy[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    energy = (energy != "0").astype(int)
    energy["SumOfAnswers"] = energy.sum(axis=1)
    energy = energy.divide(energy["SumOfAnswers"], axis=0)
    energy["Domain"] = "Energy"
    df_domains = pd.concat([df_domains, energy])

    # Engineering and Technology
    engtech = df_researchers.loc[df_researchers['disc_engtech'] == "Engineering and Technology"]
    engtech = engtech[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    engtech = (engtech != "0").astype(int)
    engtech["SumOfAnswers"] = engtech.sum(axis=1)
    engtech = engtech.divide(engtech["SumOfAnswers"], axis=0)
    engtech["Domain"] = "Engineering and Technology"
    df_domains = pd.concat([df_domains, engtech])

    # Environmental Sciences
    environ = df_researchers.loc[df_researchers['disc_environ'] == "Environmental Sciences"]
    environ = environ[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    environ = (environ != "0").astype(int)
    environ["SumOfAnswers"] = environ.sum(axis=1)
    environ = environ.divide(environ["SumOfAnswers"], axis=0)
    environ["Domain"] = "Environmental Sciences"
    df_domains = pd.concat([df_domains, environ])

    # Health Professions
    healthprof = df_researchers.loc[df_researchers['disc_healthprof'] == "Health Professions"]
    healthprof = healthprof[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    healthprof = (healthprof != "0").astype(int)
    healthprof["SumOfAnswers"] = healthprof.sum(axis=1)
    healthprof = healthprof.divide(healthprof["SumOfAnswers"], axis=0)
    healthprof["Domain"] = "Health Professions"
    df_domains = pd.concat([df_domains, healthprof])

    # Immunology and Microbiology
    immun = df_researchers.loc[df_researchers['disc_immun'] == "Immunology and Microbiology"]
    immun = immun[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    immun = (immun != "0").astype(int)
    immun["SumOfAnswers"] = immun.sum(axis=1)
    immun = immun.divide(immun["SumOfAnswers"], axis=0)
    immun["Domain"] = "Immunology and Microbiology"
    df_domains = pd.concat([df_domains, immun])

    # Materials Science
    matlsci = df_researchers.loc[df_researchers['disc_matlsci'] == "Materials Science"]
    matlsci = matlsci[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    matlsci = (matlsci != "0").astype(int)
    matlsci["SumOfAnswers"] = matlsci.sum(axis=1)
    matlsci = matlsci.divide(matlsci["SumOfAnswers"], axis=0)
    matlsci["Domain"] = "Materials Science"
    df_domains = pd.concat([df_domains, matlsci])

    # Mathematics
    math = df_researchers.loc[df_researchers['disc_math'] == "Mathematics"]
    math = math[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    math = (math != "0").astype(int)
    math["SumOfAnswers"] = math.sum(axis=1)
    math = math.divide(math["SumOfAnswers"], axis=0)
    math["Domain"] = "Mathematics"
    df_domains = pd.concat([df_domains, math])

    # Medicine
    med = df_researchers.loc[df_researchers['disc_med'] == "Medicine"]
    med = med[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    med = (med != "0").astype(int)
    med["SumOfAnswers"] = med.sum(axis=1)
    med = med.divide(med["SumOfAnswers"], axis=0)
    med["Domain"] = "Medicine"
    df_domains = pd.concat([df_domains, med])

    # Multidisciplinary
    multi = df_researchers.loc[df_researchers['disc_multi'] == "Multidisciplinary"]
    multi = multi[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    multi = (multi != "0").astype(int)
    multi["SumOfAnswers"] = multi.sum(axis=1)
    multi = multi.divide(multi["SumOfAnswers"], axis=0)
    multi["Domain"] = "Multidisciplinary"
    df_domains = pd.concat([df_domains, multi])

    # Neuroscience
    neuro = df_researchers.loc[df_researchers['disc_neuro'] == "Neuroscience"]
    neuro = neuro[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    neuro = (neuro != "0").astype(int)
    neuro["SumOfAnswers"] = neuro.sum(axis=1)
    neuro = neuro.divide(neuro["SumOfAnswers"], axis=0)
    neuro["Domain"] = "Neuroscience"
    df_domains = pd.concat([df_domains, neuro])

    # Nursing
    nurs = df_researchers.loc[df_researchers['disc_nurs'] == "Nursing"]
    nurs = nurs[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    nurs = (nurs != "0").astype(int)
    nurs["SumOfAnswers"] = nurs.sum(axis=1)
    nurs = nurs.divide(nurs["SumOfAnswers"], axis=0)
    nurs["Domain"] = "Nursing"
    df_domains = pd.concat([df_domains, nurs])

    # Pharmacology and Toxicology
    pharma = df_researchers.loc[df_researchers['disc_pharma'] == "Pharmacology and Toxicology"]
    pharma = pharma[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    pharma = (pharma != "0").astype(int)
    pharma["SumOfAnswers"] = pharma.sum(axis=1)
    pharma = pharma.divide(pharma["SumOfAnswers"], axis=0)
    pharma["Domain"] = "Pharmacology and Toxicology"
    df_domains = pd.concat([df_domains, pharma])

    # Physics
    physics = df_researchers.loc[df_researchers['disc_physics'] == "Phsyics"]
    physics = physics[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    physics = (physics != "0").astype(int)
    physics["SumOfAnswers"] = physics.sum(axis=1)
    physics = physics.divide(physics["SumOfAnswers"], axis=0)
    physics["Domain"] = "Physics"
    df_domains = pd.concat([df_domains, physics])

    # Psychology
    psych = df_researchers.loc[df_researchers['disc_psych'] == "Psychology"]
    psych = psych[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    psych = (psych != "0").astype(int)
    psych["SumOfAnswers"] = psych.sum(axis=1)
    psych = psych.divide(psych["SumOfAnswers"], axis=0)
    psych["Domain"] = "Psychology"
    df_domains = pd.concat([df_domains, psych])

    # Social Science
    socsci = df_researchers.loc[df_researchers['disc_socsci'] == "Social Science"]
    socsci = socsci[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    socsci = (socsci != "0").astype(int)
    socsci["SumOfAnswers"] = socsci.sum(axis=1)
    socsci = socsci.divide(socsci["SumOfAnswers"], axis=0)
    socsci["Domain"] = "Social Science"
    df_domains = pd.concat([df_domains, socsci])

    # Veterinary
    vet = df_researchers.loc[df_researchers['disc_vet'] == "Veterinary"]
    vet = vet[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    vet = (vet != "0").astype(int)
    vet["SumOfAnswers"] = vet.sum(axis=1)
    vet = vet.divide(vet["SumOfAnswers"], axis=0)
    vet["Domain"] = "Veterinary"
    df_domains = pd.concat([df_domains, vet])

    # Information Science
    infosci = df_researchers.loc[df_researchers['disc_infosci'] == "Information Science"]
    infosci = infosci[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    infosci = (infosci != "0").astype(int)
    infosci["SumOfAnswers"] = infosci.sum(axis=1)
    infosci = infosci.divide(infosci["SumOfAnswers"], axis=0)
    infosci["Domain"] = "Information Science"
    df_domains = pd.concat([df_domains, infosci])

    # Other
    other = df_researchers.loc[df_researchers['disc_other'] == "Other"]
    other = other[["Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    other = (other != "0").astype(int)
    other["SumOfAnswers"] = other.sum(axis=1)
    other = other.divide(other["SumOfAnswers"], axis=0)
    other["Domain"] = "Other"

    df_domains = pd.concat([df_domains, other])

    df_domains_type = df_domains[["Domain", "Observational/Empirical", "Experimental Need", "Simulation", "Derived/Compiled", "Other Needs"]]
    df_domains_usage = df_domains[["Domain", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]

    df_domains["SumOfAnswersTotal"] = df_domains.sum(axis=1)
    df_domains_type["SumOfAnswersTotal"] = df_domains_type.sum(axis=1)
    df_domains_usage["SumOfAnswersTotal"] = df_domains_usage.sum(axis=1)

    # map domain to correct dataframe
    if domain == "agricul": domain = agriculture
    elif domain == "artshuman": domain = artshuman
    elif domain == "biochem": domain = biochem
    elif domain == "bio": domain = biological
    elif domain == "busin": domain = busin_df
    elif domain == "chemeng": domain = chemeng
    elif domain == "compsci": domain = compsci
    elif domain == "chem": domain = chem
    elif domain == "decisci": domain = decisionsci
    elif domain == "dentist": domain = dentist
    elif domain == "earth": domain = earthplanet
    elif domain == "econ": domain = econ
    elif domain == "energy": domain = energy
    elif domain == "engtech": domain = engtech
    elif domain == "environ": domain = environ
    elif domain == "health": domain = healthprof
    elif domain == "immun": domain = immun
    elif domain == "matlsci": domain = matlsci
    elif domain == "math": domain = math
    elif domain == "med": domain = med
    elif domain == "multi": domain = multi
    elif domain == "neuro": domain = neuro
    elif domain == "nurs": domain = nurs
    elif domain == "pharma": domain = pharma
    elif domain == "physics": domain = physics
    elif domain == "psych": domain = psych
    elif domain == "socsci": domain = socsci
    elif domain == "vet": domain = vet
    elif domain == "infosci": domain = infosci
    elif domain == "oth": domain = other
    
    # plot heatmap
    plt.figure(figsize=(10,10))
    plt.title("Correlation between users only choosing the Domain with the data needs and usages")
    corr = domain.loc[:, domain.columns != "SumOfAnswers"].corr()
    kot = corr[corr>=.25]
    sns.heatmap(corr, cmap="Blues", linewidth=.5)
    plt.savefig('correlationVisualization/static/correlationVisualization/images/heatmap.png', bbox_inches = 'tight')
    plt.close()

    # Get top correlations
    return get_top_abs_correlations(domain.loc[:, domain.columns != "Domain"], amount)
