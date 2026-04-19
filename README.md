# Teiko Technical Assessment

This project builds a reproducible data pipeline to analyze immune cell population data and presents results through an interactive dashboard.

----------

## Overview
1. **Data Loading**
  - Loads 'cell-count.csv' into a SQLite database

2. **Data Analysis**
  - Computes total cell counts per sample
  - Calculates relative frequencies of immune cell populations
  - Performs statistical analysis comparing responders vs non-responders
  - Generates summary tables and visualizations

3. **Dashboard**
  - Provides an interactive dashboard to explore analysis results

----------

## Project Structure
|-- load_data.py # Loads CSV data into SQLite database
|-- analyze_data.py # Performs analysis and generates outputs
|-- dashboard.py # Streamlit interactive dashboard
|-- Makefile # Pipeline automation
|-- requirements.txt # Python Libraries required
|-- cell-count.csv # Input dataset
|__ outpits/ # Generated tables and plots

----------

## Setup and Execution
Run the following commands from the project root:

  ### Install dependencies
  'make setup'

  ### Run the full pipeline
  'make pipeline'
  This will:
    - Create the SQLite database
    - Perform all analysis
    - Generate output tables and plots in the 'outputs/' directory

  ### Launch Dashboard
  'make dashboard'
  Then open the provided local URL in your browser.

----------

## Database Structure

The SQLite database contains a single table:

### `cell_count`
Each row represents a sample with associated metadata and immune cell counts

**Columns include:**
- `sample`: unique sample identifier
- `project`: study or dataset source
- `subject`: subject identifier
- `condition`, `treatment`, `sample_type`: experimental metadata
- `response`, `sex`: subject characteristics
- `time_from_treatment_start`: timepoint
- `b_cell`, `cd8_t_cell`, `cd4_t_cell`, `nk_cell`, `monocyte`: cell population counts

### Design Choices

- A single table schema was chosen because the dataset is already structured with one row per sample
- This makes it straightforward to query and analyze the data
- For larger datasets (e.g., hundreds of projects and thousands of samples), the structure could be normalized into:
  - a **samples table** (metadata)
  - a **cell_counts table** (long format per population)
- This would reduce repeated data and make more complex queries

----------

## Analysis Approach

### Part 2: Initial Analysis
- Computed total cell counts per sample
- Transformed data into long format to analyze populations individually
- Calculated relative frequency (%) of each cell population

### Part 3: Statistical Analysis
- Filtered dataset to melanoma PBMC samples treated with Miraclib
- Compared responders vs non-responders
- Visualized differences using boxplots
- Performed Mann–Whitney U tests for statistical significance

### Part 4: Subset Analysis
- Focused on baseline samples (time = 0).
- Summarized:
  - samples per project
  - subjects by response
  - subjects by sex
- Computed average B cell counts for melanoma male responders.

----------

## Dashboard
The Streamlit dashboard allows users to:
- Explore processed analysis tables
- View statistical results
- Visualize cell population distributions
- Interact with filtered subsets of the data




