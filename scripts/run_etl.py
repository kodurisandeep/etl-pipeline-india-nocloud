# run_etl.py

import logging
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
import sqlite3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log"),
        logging.StreamHandler()
    ]
)


def main():
    csv_path = "data/UPVillageSchedule.csv"
    db_path = "database.db"

    logging.info("ETL process started.")
    df = extract_data(csv_path)
    if not df.empty:
        transformed_df = transform_data(df)
        load_data(transformed_df, db_path)
        validate_load(db_path)
        logging.info("ETL process completed successfully.")
    else:
        logging.warning("No data extracted. Terminating ETL process.")

def validate_load(db_path: str, table_name: str = "irrigation_data"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    logging.info(f"Validation: {count} records found in '{table_name}' table.")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
    ##test
    rows = cursor.fetchall()
    for row in rows:
        logging.info(row)
    conn.close()

if __name__ == "__main__":
    main()
