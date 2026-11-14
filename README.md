# ResearchMate Agent

A Streamlit prototype for comparing research papers, drafting literature reviews and asking questions against page-linked PDF excerpts.

## Run locally

Use Python 3.11 or later in a virtual environment, install `pip install -r requirements.txt`, set `OPENAI_API_KEY` in your local environment, then run `streamlit run app.py`. Do not commit keys or uploaded papers. Processing sends paper text to OpenAI and can incur API charges.

## Verification

Run `python -m unittest discover -v`. Fourteen offline validation and citation-provenance tests passed during the November 2026 source review. These tests check output shape and trusted file identity, not model accuracy. No live model calls or hosted end-to-end session were verified.

## Current limits

Long papers are sampled rather than fully analyzed. Retrieved passages carry page numbers, and Q&A claims must now include a source ID and an exact excerpt. Unknown source IDs and invented quotations are rejected. This validates quotation provenance, not whether the excerpt logically supports the claim. Failed model requests still need a polished recovery flow. Treat reviews and research gaps as drafts for human review.

## Source history

The original March 8, 2026 upload is retained as `researchmate-agent.zip`. The expanded source adds strict analysis validation clears previous results before processing a new collection, and checks Q&A quotation provenance. Implementation and review used AI assistance. Upstream libraries: Streamlit, OpenAI Python SDK, pypdf, pandas and NumPy; their licenses remain applicable.
