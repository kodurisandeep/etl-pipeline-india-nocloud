# extract.py
import logging
import pandas as pd

def extract_data(csv_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(csv_path)
        logging.info(f"Data extracted: {df.shape[0]} records")
        return df
    except FileNotFoundError:
        logging.warning("CSV file not found.")
        return pd.DataFrame()