India Irrigation ETL Pipeline
A lightweight Python-based ETL pipeline that extracts, transforms, and loads agricultural irrigation data for India into a local SQLite database. Includes automated GitHub CI/CD, timestamp-based version tagging, and changelog generation.

📂 Project Structure
etl-pipeline-india-nocloud/
├── data/
│   └── rawcsvdataset.csv
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── run_etl.py
│   └── __init__.py
├── database.db
├── requirements.txt
├── CHANGELOG.md
├── .gitignore
└── .github/
    └── workflows/
        ├── etl-pipeline.yml
        ├── tag-on-main.yml
        └── changelog.yml

🛠️ Tools Used
- Python 3.11+
- Pandas
- SQLite
- GitHub Actions
- GitHub CLI (gh)
- Git & GitHub
- github-changelog-generator (Ruby gem)

🚀 How to Run Locally
# Setup
python -m venv venv
source venv/bin/activate       # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

# Run ETL
$env:PYTHONPATH = "."; python scripts/run_etl.py


✅ Output
- database.db SQLite file with 106,000+ cleaned irrigation records
- etl.log file for process tracing
🔍 Data Fields
Includes state, district, block, village, irrigation stats across seasons, groundwater levels, and scheme types
📄 Original Dataset Source

🔁 Git Branching Strategy
| Environment | Git Branch | 
| Dev (Local) | — | 
| Dev Integration | dev | 
| SIT/UAT | sit | 
| Production | main | 


Promotion flow: dev → sit → main via pull requests and CI checks.

⚙️ GitHub Workflows
✅ etl-pipeline.yml
Runs on: dev, sit, main
- Validates ETL logic by running scripts/run_etl.py
- Automatically checks integrity at each branch stage
🏷️ tag-on-main.yml
Runs on: Push to main
- Tags each release with a timestamp (vYYYYMMDD-HHMMSS)
- Publishes a GitHub release
- Uses PAT_TOKEN for authentication via CLI
📘 changelog.yml
Runs on: Push to main or manual trigger
- Generates CHANGELOG.md from PRs, commits, and authors
- Uses github-changelog-generator and pushes update automatically

🛡️ Branch Protection
Recommended rules (on GitHub Settings → Branches):
- Require pull requests to merge into main
- Require status checks to pass (ETL Pipeline Check)
- Prevent force pushes and deletions

🔑 GitHub Secrets
| Name | Purpose | 
| PAT_TOKEN | Enables tagging and changelog updates from Actions | 



🗃️ .gitignore Suggestion
*.db
*.log
__pycache__/
.env
