# India Irrigation ETL Pipeline

A lightweight Python-based ETL pipeline that extracts, transforms, and loads agricultural irrigation data for India into a local SQLite database.

## 📂 Project Structure

india_etl/ ├── data/ │ └── rawcsvdataset.csv ├── scripts/ │ ├── extract.py │ ├── transform.py │ ├── load.py │ ├── run_etl.py │ └── init.py ├── database.db ├── requirements.txt ├── .gitignore └── README.md


## 🛠️ Tools Used

- Python 3.11+
- Pandas
- SQLite
- Logging
- Git & GitHub

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
$env:PYTHONPATH = "."; python scripts/run_etl.py

✅ Output
- database.db SQLite file with 106,000+ cleaned irrigation records
- etl.log file for process tracing
🔍 Data Fields
Includes state, district, block, village, irrigation stats across seasons, groundwater levels, and scheme types.
CSV Link: https://www.data.gov.in/resource/6th-minor-irrigation-census-village-schedule-uttar-pradesh

---

### 🔧 Step 2: Create `.gitignore`

```gitignore
*.db
*.log
__pycache__/
.env