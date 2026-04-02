"""
(MY EDITED COPY OF THIS FILE)

Source: validated JSON object
Sink: Polars DataFrame

Purpose

  Transform validated JSON data into a structured format.

Analytical Questions

- Which fields are needed from the JSON data?
- How can records be normalized into tabular form?
- What derived fields would support analysis?

Notes

Following our process, do NOT edit this _case file directly,
keep it as a working example.

In your custom project, copy this _case.py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- extract the fields needed for your analysis,
- normalize records into a consistent structure,
- create any derived fields required.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import os
from typing import Any

os.environ["POLARS_SKIP_CPU_CHECK"] = "1"
import polars as pl

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform JSON into a structured DataFrame.

    Args:
        json_data (list[dict[str, Any]]): Validated JSON data.
        LOG (logging.Logger): The logger instance.

    Returns:
        pl.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    records: list[dict[str, Any]] = []

    for record in json_data:
        records.append(
            {
                "title": record.get("title"),
                "author": record.get("author"),
                "description": record.get("description"),
                "content": record.get("content"),
                "source": record.get("source", {}).get("name"),
            }
        )

    df: pl.DataFrame = pl.DataFrame(records)

    # ============================================================
    # TECHNICAL MOD: define reusable text field (future-proofing)
    # ============================================================

    # TECH MOD (Phase 4 legacy):
    # text = pl.col("content")
    # NOTE: Previously used as reusable reference for word_count,
    # but replaced in Phase 5 by "content_clean" for improved data quality.

    # First: clean content properly (so all later features use clean text)
    df = df.with_columns(
        [
            pl.col("content")
            .fill_null("")
            .str.replace_all(r"\[\+\d+\schars\]", "")
            .str.strip_chars()
            .alias("content_clean")
        ]
    )

    # Derived fields
    df = df.with_columns(
        [
            # ----------------------------
            # Length metrics
            # ----------------------------
            pl.col("title").str.len_chars().alias("title_length"),
            pl.col("content_clean").str.len_chars().alias("content_length"),
            # ----------------------------
            # Word count
            # ----------------------------
            pl.col("content_clean")
            .fill_null("")
            .str.split(" ")
            .list.len()
            .alias("word_count"),
            # ----------------------------
            # has_author flag
            # ----------------------------
            pl.when(pl.col("author").is_not_null() & (pl.col("author") != ""))
            .then(True)
            .otherwise(False)
            .alias("has_author"),
            # ----------------------------
            # Article length category
            # ----------------------------
            pl.when(pl.col("content_clean").str.len_chars() < 150)
            .then(pl.lit("short"))
            .when(pl.col("content_clean").str.len_chars() < 300)
            .then(pl.lit("medium"))
            .otherwise(pl.lit("long"))
            .alias("article_length_category"),
        ]
    )

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Polars DataFrame created")

    # Return the transformed DataFrame for use in the next stage.
    return df
