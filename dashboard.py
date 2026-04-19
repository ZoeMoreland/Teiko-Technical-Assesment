import os
import pandas as pd 
import streamlit as st 

OUTPUT_DIR = "outputs"

def main():
    st.title("Cell Count Analysis Dashboard")
    st.write("Interactive dashboard showing results from the analysis pipeline.")
    
    # Initial analysis table
    initial_analysis_path = os.path.join(OUTPUT_DIR, "initial_analysis.csv")
    if os.path.exists(initial_analysis_path):
        initial_df = pd.read_csv(initial_analysis_path)
        st.subheader("Initial Analysis Table")
        populations = sorted(initial_df["population"].dropna().unique())
        selected_population = st.selectbox("Filter by cell population", populations)
        filtered_initial = initial_df[initial_df["population"] == selected_population]
        st.dataframe(filtered_initial)
        

    # Boxplot
    boxplot_path = os.path.join(OUTPUT_DIR, "cell_population_frequencies_boxplot.png")
    if os.path.exists(boxplot_path):
        st.subheader("Responders vs Non-Responders Boxplot")
        st.image(boxplot_path)
        
    
    # Significance results
    sig_path = os.path.join(OUTPUT_DIR, "significance_results.csv")
    if os.path.exists(sig_path):
        sig_df = pd.read_csv(sig_path)
        st.subheader("Statistical Significance Results")
        st.dataframe(sig_df)
        
        
    # Baseline Summaries
    samples_project_path = os.path.join(OUTPUT_DIR, "samples_per_project.csv")
    if os.path.exists(samples_project_path):
        samples_project_df = pd.read_csv(samples_project_path)
        st.subheader("Baseline Samples per Project")
        st.dataframe(samples_project_df)
        
        
    subjects_response_path = os.path.join(OUTPUT_DIR, "subjects_by_response.csv")
    if os.path.exists(subjects_response_path):
        subjects_response_df = pd.read_csv(subjects_response_path)
        st.subheader("Baseline Subjects by Response")
        st.dataframe(subjects_response_df)
        
    
    subjects_sex_path = os.path.join(OUTPUT_DIR, "subjects_by_sex.csv")
    if os.path.exists(subjects_sex_path):
        subjects_sex_df = pd.read_csv(subjects_sex_path)
        st.subheader("Baseline Subjects by Sex")
        st.dataframe(subjects_sex_df)
        
        
if __name__ == "__main__":
    main()