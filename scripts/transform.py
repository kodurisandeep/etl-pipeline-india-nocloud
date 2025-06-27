# transform.py
import pandas as pd
import logging

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.dropna(subset=["state_name", "district_name"])
    df["gross_irrigated_area_total"] = pd.to_numeric(df["gross_irrigated_area_total"], errors="coerce")
    logging.info(f"Data transformed: {df.shape[0]} records remaining")
    return df