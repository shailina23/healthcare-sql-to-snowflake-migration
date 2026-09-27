# Healthcare SQL → Snowflake Migration Lab

> Legacy reporting logic translated into a cloud-warehouse pattern with reconciliation.

## Project status
**Portfolio / synthetic client-style project.** The datasets and business names are fictional and were created for demonstration. The engineering patterns are designed to be realistic and reusable.

## Business problem
An imaginary healthcare reporting team has monthly revenue logic embedded in a legacy SQL workload. The goal is to preserve business logic while moving raw data into Snowflake-style layers and producing a clean analytics view.

## Architecture
`Legacy SQL → RAW tables → CURATED view → reconciliation → BI-ready dataset`

## What this demonstrates
- Production-style data engineering structure
- Clear source-to-target mappings
- Reproducible transformations
- Data-quality / reconciliation checks
- Business-facing documentation
- A realistic handover path

## How to run
1. Install Python + pandas. 2. Run `python scripts/run_reconciliation.py`. 3. Review the legacy query under `sql/legacy/`. 4. Review Snowflake DDL/views under `sql/snowflake/`. 5. Load the CSVs into a Snowflake trial account if you want a live cloud demo.

## Repository structure
`data/` = synthetic source data
`sql/legacy/` = old reporting logic
`sql/snowflake/` = target DDL and analytics view
`scripts/` = reconciliation automation
`docs/` = mapping and architecture

## Business value
Demonstrates migration discovery, SQL translation, target modeling, and control-total validation — the exact conversation a client needs to have before trusting a migration.

## Important note
This is a portfolio simulation, not a claim that the fictional healthcare organization was a real client.
