import sqlite3
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu


def main():
    conn = sqlite3.connect("cell-count.db")

    cell_count_df = pd.read_sql("SELECT * FROM cell_count", conn)
    
    # PART 2: Initial Analysis - Data Overview
    # Calculate total_count as sum of the 5 cell types
    cell_count_df['total_count'] = cell_count_df[['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']].sum(axis=1)
    
    # Create summary analysis dataframe by melting tp create one row per sample per population
    initial_analysis = cell_count_df.melt(id_vars=['sample', 'total_count'],
                                          value_vars=['b_cell', 'cd8_t_cell', 
                                                      'cd4_t_cell', 'nk_cell', 'monocyte'], 
                                          var_name='population',
                                          value_name='count')
    
    initial_analysis = pd.merge(initial_analysis, cell_count_df[['sample', 'response']], on='sample', how='left')
    
    # Calculate percentage of relative frequency
    initial_analysis['percentage'] = (initial_analysis['count'] / initial_analysis['total_count']) * 100

    print(initial_analysis.head())
    
    
    # PART 3: Statistical Analysis
    filtered_df = cell_count_df[(cell_count_df['condition'] == 'melanoma') &
                                (cell_count_df['treatment'] == 'miraclib') &
                                (cell_count_df['sample_type'] == 'PBMC')]
    
    filtered_samples = filtered_df['sample'].unique()
    analysis_df = initial_analysis[initial_analysis['sample'].isin(filtered_samples)]
    
    # Boxplot
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=analysis_df, x='population', y='percentage', hue='response')
    plt.title('Cell Population Frequencies: Responders vs Non-Responders (Melanoma, Miraclib, PBMC)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("cell_population_frequencies_boxplot.png")
    plt.show()
    
    # Statistical Significance
    results = []
    for pop in analysis_df['population'].unique():
        responders = analysis_df[(analysis_df['population'] == pop) & (analysis_df['response'] == 'yes')]['percentage']
        non_responders = analysis_df[(analysis_df['population'] == pop) & (analysis_df['response'] == 'no')]['percentage']
    
        if len(responders) > 0 and len(non_responders) > 0:
            stat, p_value = mannwhitneyu(responders, non_responders, alternative='two-sided')
            results.append({'population': pop, 'p_value': p_value, 'significant': 'Yes' if p_value < 0.05 else 'No'})
    
    significance_df = pd.DataFrame(results)
    print("\nStatistical Significance Results:")
    print(significance_df)
    
    
    # PART 4: Data Subset Analysis
    query = """
    SELECT * FROM cell_count
    WHERE condition = 'melanoma' AND treatment = 'miraclib AND 
    sample_type = 'PBMC AND time_from_treatment = 0     

    """    
    baseline_df = pd.read_sql(query, conn)
    
    print("\nPart 4: Baseline Melanoma PBMC Samples on Miraclib")
    print(f"Total baseline samples: {len(baseline_df)}")
    
    # Samples per Project
    samples_per_project = baseline_df.groupby('project')['sample'].count()
    print("\nSsamples per project:", samples_per_project)
    
    # Subjects by Response
    subjects_by_response = baseline_df.drop_duplicates('subjects').groupby('response')['subject'].count()
    print("\nSubjects by response:", subjects_by_response)
    
    # Subjects by sex
    subjects_by_sex = baseline_df.drop_duplicates('subjects').groupby('sex')['subject'].count()
    print("\nSubjects by sex:", subjects_by_sex)
    
    
    
    conn.close()
    
if __name__ == "__main__":
    main()