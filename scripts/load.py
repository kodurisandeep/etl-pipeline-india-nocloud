# load.py
import sqlite3
import pandas as pd
import logging

def load_data(df: pd.DataFrame, db_path: str, table_name: str = "irrigation_data"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    logging.info(f"Data loaded into {db_path}, table: {table_name}")