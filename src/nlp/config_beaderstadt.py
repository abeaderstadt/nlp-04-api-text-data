"""
config_case.py
(EDIT YOUR COPY OF THIS FILE)

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- What API endpoint should be used as the data source?
- What HTTP request headers are required?
- Where should raw and processed data be stored?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project,copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to change:
- API URL (source of the JSON data),
- the HTTP Request Headers (to show your app name in the user-agent header)
- customize your output file name.
"""

import os
from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("Please set your NEWS_API_KEY environment variable")

API_URL: str = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-beaderstadt/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"


RAW_JSON_PATH: Path = RAW_PATH / "beaderstadt_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "beaderstadt_processed.csv"
