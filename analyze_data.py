import sqlite3
import pandas as pd 


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
    
    conn.close()
    
if __name__ == "__main__":
    main()