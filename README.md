# nlp-01-getting-started

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for Web Mining and Applied NLP.

Web Mining and Applied NLP focus on retrieving, processing, and analyzing text from the web and other digital sources.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows a similar structure based on professional Python projects.
These projects are **hands-on textbooks** for learning Web Mining and Applied NLP.

## This Project

This project focuses on retrieving and processing structured text data
**from web APIs in JSON format**.

The goal is to acquire JSON data from an external source,
inspect and validate its structure,
transform it into a usable format,
and load it into a reproducible output.

You've likely heard of ETL or ELT.
We recommend EVTL.

In EVTL, each stage has a source, a process, and a sink.

- **Extract** acquires data
- **Validate** inspects and checks it
- **Transform** reshapes it
- **Load** sends it to the chosen destination

This project illustrates how to **work with real API data and understand its structure before analysis**.

## Key Files

You'll work with these files as you update authorship and experiment:

- **src/nlp/pipeline_api_json.py** - MAIN PIPELINE SCRIPT (no changes needed)
- **src/nlp/config_case.py** - Python configuration (<mark>**copy and edit**</mark> for your custom project)
- **src/nlp/stage01_extract.py** - EXTRACT (no changes needed)
- **src/nlp/stage02_validate_case.py** - VALIDATE (<mark>**copy and edit**</mark>)
- **src/nlp/stage03_transform_case.py** - TRANSFORM (<mark>**copy and edit**</mark>)
- **src/nlp/stage04_load.py** - LOAD (no changes needed)
- **pyproject.toml** - <mark>**update**</mark> authorship, links, and dependencies
- **zensical.toml** - <mark>**update**</mark> authorship and links

## First: Follow These Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**

## Success

After running the script successfully, you will see:


```shell
========================
Pipeline executed successfully!
========================
```

And new files will appear:

- project.log - confirming successful run
- data/raw/case_raw.json - dump of the fetched JSON
- data/processed/case_processed.csv - final loaded result

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/abeaderstadt/nlp-04-api-text-data
cd nlp-04-api-text-data
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# Later, we install spacy data model and
# en_core_web_sm = english, core, web, small
# It's big: spacy+data ~200+ MB w/ model installed
#           ~350–450 MB for .venv is normal for NLP
# uv run python -m spacy download en_core_web_sm

# First, run the module
# IMPORTANT: Close each figure after viewing so execution continues
uv run python -m nlp.pipeline_api_json

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## My Project Modifications

To make this project my own, I extended the example ETL pipeline to work with a live API (NewsAPI) and added structured validation and transformation steps to support real-world JSON data.

**Phase 4: Make a Technical Modification**
1. I added a new feature called word_count in the Transform stage of the pipeline.
2. It takes the body (or content field), splits it into words, and counts how many words are in each post.
3. Observations:
     - Posts with a character length around ~180-200 usually had word counts in the mid-teens to high twenties.
     - There is a pretty consistent relationship between how long something looks and how much it actually says.
     - character count = raw size of the text.
     - word_count = more “human” sense of information content.
     - Adding word_count makes it much easier to compare posts in a more meaningful way instead of just looking at raw text length.

**Phase 5: Apply the Skills to a New Problem**
1. Refactored the pipeline so it works cleanly with new live API data (NewsAPI instead of example data).
2. Moved the API key out of the code and into environment variables instead of hardcoding it. This keeps sensitive info out of the repo and makes the project safer to push to GitHub.
3. Updated the validation stage to handle real-world JSON structure (nested articles field).
4. Added three transformation improvements:
     - Cleaned the content field by removing API artifacts such as [+774 chars]
     - Added a has_author flag to measure completeness of metadata across articles
     - Created article length categories to support future analysis and dashboard-friendly grouping
5. Confirmed the full pipeline runs end-to-end and outputs a clean CSV file in data/processed/.
6. Observations:
     - This pipeline now feels like a real ETL system not just a script. Each step depends on the previous one in a clean, predictable way.
     - Handling real API data created challenges such as inconsistent fields, missing values, and noisy text which then needed extra transformation.
     - The addition of derived features (has_author, length categories, and cleaned content) will help with future analysis and visualization work.

**Dataset Source**
1. Get a free API key from https://newsapi.org
2. Set your environment variable:
   - Windows (PowerShell): setx NEWS_API_KEY "your_api_key_here"
3. Restart terminal
4. Run the pipeline script
    - Windows (Powershell): uv run python -m nlp.pipeline_api_json

## Example Artifact (Output)


```text
START PIPELINE
ROOT_PATH = .
DATA_PATH = data
RAW_PATH = data\raw
PROCESSED_PATH = data\processed
========================
STAGE 01: EXTRACT starting...
========================
SOURCE PATH = https://jsonplaceholder.typicode.com/posts
SINK PATH = data\raw\case_raw.json
========================
STAGE 02: VALIDATE starting...
========================
JSON STRUCTURE INSPECTION:
Top-level type: list
Keys in first record: ['userId', 'id', 'title', 'body']
Field types:
userId: int
id: int
title: str
body: str
Validation passed.
Sink: validated JSON object
========================
STAGE 03: TRANSFORM starting...
========================
Transformation complete.
DataFrame preview:
shape: (5, 6)
...preview of dataframe...
Sink: Polars DataFrame created
========================
STAGE 04: LOAD starting...
========================
SINK PATH = data\processed\case_processed.csv
========================
Pipeline executed successfully!
========================
```


## Enhancements

In production systems, validation is often automated using tools
such as Great Expectations or Soda.

In this module, validation is implemented manually to develop a
clear understanding of structure, assumptions, and data quality.
