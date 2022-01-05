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
    return au_corr[0:n].round(2)

def plotHeatmap(domain, amount):
    global df_domain
    # map domain to correct domain name
    if domain == "disc_agricul": domainName = "Agriculture"
    elif domain == "disc_astronom": domainName = "Astronomy"
    elif domain == "disc_artshuman": domainName = "Arts and Humanities"
    elif domain == "disc_biochem": domainName = "Biochemistry, Genetics, Molecular Biology"
    elif domain == "disc_biological": domainName = "Biological Sciences"
    elif domain == "disc_busin": domainName = "Business"
    elif domain == "disc_chemeng": domainName = "Chemical Engineering"
    elif domain == "disc_compsci": domainName = "Computer Sciences, IT"
    elif domain == "disc_chem": domainName = "Chemistry"
    elif domain == "disc_decisionsci": domainName = "Decision Sciences"
    elif domain == "disc_dentist": domainName = "Dentistry"
    elif domain == "disc_earthplanet": domainName = "Earth and Planetary Sciences"
    elif domain == "disc_econ": domainName = "Economics and Finance"
    elif domain == "disc_energy": domainName = "Energy"
    elif domain == "disc_engtech": domainName = "Engineering and Technology"
    elif domain == "disc_environ": domainName = "Environmental Sciences"
    elif domain == "disc_healthprof": domainName = "Health Professions"
    elif domain == "disc_immun": domainName = "Immunology and Microbiology"
    elif domain == "disc_matlsci": domainName = "Materials Science"
    elif domain == "disc_math": domainName = "Mathematics"
    elif domain == "disc_med": domainName = "Medicine"
    elif domain == "disc_multi": domainName = "Multidisciplinary"
    elif domain == "disc_neuro": domainName = "Neuroscience"
    elif domain == "disc_nurs": domainName = "Nursing"
    elif domain == "disc_pharma": domainName = "Pharmacology and Toxicology"
    elif domain == "disc_physics": domainName = "Physics"
    elif domain == "disc_psych": domainName = "Psychology"
    elif domain == "disc_socsci": domainName = "Scoial Sciences"
    elif domain == "disc_vet": domainName = "Veterinary"
    elif domain == "disc_infosci": domainName = "Information Science"
    elif domain == "disc_other": domainName = "Other"
    elif domain == "compsci_engtech": domainName = "Computer Science, IT - Engineering Technologies"
    elif domain == "biochem_bio": domainName = "Biochemistry - Biological Sciences"
    elif domain == "environ_bio": domainName = "Environmental Sciences - Biological Sciences"
    elif domain == "med_health": domainName = "Medicine - Health Professions"
    

    # load data
    df_researchers = pd.read_csv('/Users/mehmetgoksen/Library/Mobile Documents/com~apple~CloudDocs/Uni/BA/Scripts/correlationAnalysis/correlationVisualization/datadiscovery_researchers.csv')

    # Get users with single domains
    df_single_domain_researchers = df_researchers[["disc_agricul", "disc_artshuman", "disc_astronom", "disc_biochem", "disc_biological", "disc_busin", "disc_chemeng", "disc_chem", "disc_compsci", "disc_decisionsci", "disc_dentist", "disc_earthplanet", "disc_econ", "disc_energy", "disc_engtech", "disc_environ", "disc_healthprof", "disc_immun", "disc_matlsci", "disc_math", "disc_med", "disc_multi", "disc_neuro", "disc_nurs", "disc_pharma", "disc_physics", "disc_psych", "disc_socsci", "disc_vet", "disc_infosci", "disc_other"]]

    df_single_domain_researchers = (df_single_domain_researchers != "0").astype(int)
    df_single_domain_researchers["sum"] = df_single_domain_researchers.sum(axis=1)

    # rename columns
    df_researchers = df_researchers.rename(columns={"need_obs": "Observational/Empirical (Type)", "need_exp": "Experimental (Type)", "need_sim": "Simulation (Type)", "need_deriv": "Derived/Compiled (Type)", "need_oth": "Other Types", "use_nwstdy": "Basis for new study", "use_calb" : "Calibration", "use_bnchmrk" : "Benchmarking", "use_vrfctn" : "Verification", "use_inpt" : "Input", "use_idea": "Generating new ideas", "use_tch": "Teaching", "use_nwprj" : "Prepare new project/proposal", "use_nwmth" : "Experimental Use", "use_trnds" : "Identifying trends/predictions", "use_cmprsn" : "Comparison", "use_smvs" : "Summarizations", "use_intgrtn" : "Integrate with other data", "use_oth" : "Other Uses"})

    # Get Data into Dataframe
    if domain == "compsci_engtech": 
        df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==2]
        df_researchers = df_researchers.iloc[df_index.index, :]
        df_domain = df_researchers.loc[(df_researchers['disc_compsci'] == "Computer Sciences, IT") & (df_researchers['disc_engtech'] == "Engineering and Technology")]
    elif domain == "biochem_bio":
        df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==2]
        df_researchers = df_researchers.iloc[df_index.index, :]
        df_domain = df_researchers.loc[(df_researchers['disc_biochem'] == "Biochemistry, Genetics, Molecular Biology") & (df_researchers['disc_biological'] == "Biological Sciences")]
    elif domain == "environ_bio":
        df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==2]
        df_researchers = df_researchers.iloc[df_index.index, :]
        df_domain = df_researchers.loc[(df_researchers['disc_environ'] == "Environmental Sciences") & (df_researchers['disc_biological'] == "Biological Sciences")]
    elif domain == "med_health":
        df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==2]
        df_researchers = df_researchers.iloc[df_index.index, :]
        df_domain = df_researchers.loc[(df_researchers['disc_med'] == "Medicine") & (df_researchers['disc_healthprof'] == "Health Professions")]
    else:
        df_index = df_single_domain_researchers.loc[df_single_domain_researchers["sum"]==1]
        df_researchers = df_researchers.iloc[df_index.index, :]
        df_domain = df_researchers.loc[df_researchers[domain] == domainName]
    df_domain = df_domain[["Observational/Empirical (Type)", "Experimental (Type)", "Simulation (Type)", "Derived/Compiled (Type)", "Other Types", "Basis for new study", "Calibration", "Benchmarking", "Verification", "Input", "Generating new ideas", "Teaching", "Prepare new project/proposal", "Experimental Use", "Identifying trends/predictions", "Comparison", "Summarizations", "Integrate with other data", "Other Uses"]]
    df_domain = (df_domain != "0").astype(int)
    df_domain["SumOfAnswers"] = df_domain.sum(axis=1)
    df_domain = df_domain.divide(df_domain["SumOfAnswers"], axis=0)
    df_domain["Domain"] = domainName

    corr = df_domain.loc[:, df_domain.columns != "SumOfAnswers"].corr().abs().unstack().round(2)
    corr = pd.DataFrame(corr)
    corr.to_csv("correlationVisualization/static/correlationVisualization/files/correlations.csv")
    corr = pd.read_csv("correlationVisualization/static/correlationVisualization/files/correlations.csv")
    corr.columns=["Group1", "Group2", "Value"]
    corr.to_csv("correlationVisualization/static/correlationVisualization/files/correlations.csv")
    
    # Get top correlations
    return get_top_abs_correlations(df_domain.loc[:, df_domain.columns != "Domain"], amount)

def getDomainName():
    if len(df_domain.index > 0):
        return df_domain.iloc[0]["Domain"]

def getSampleSize():
    return len(df_domain.index)