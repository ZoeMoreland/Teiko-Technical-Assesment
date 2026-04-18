import sqlite3
import pandas as pd


def main():
    # Load cell_count.csv as dataframe
    cell_count_df = pd.read_csv("cell-count.csv")

    # Connect to SQLite database
    conn_cell_count = sqlite3.connect("cell-count.db")

    # Dataframe writing to SQLite database
    cell_count_df.to_sql("cell_count", conn_cell_count, if_exists="replace", index=False)

    conn_cell_count.commit()
    conn_cell_count.close()
    



if __name__ == "__main__":
    main()