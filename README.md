# Healthcare SQL → Snowflake Migration Lab

A synthetic portfolio project exploring how to document and migrate a legacy healthcare reporting workflow toward a Snowflake-style analytics model.

> **Project status:** Foundation stage. This repository currently contains synthetic source data and its data dictionary. SQL transformations, target models, and reconciliation code are planned next.

## Scenario

A fictional healthcare reporting team needs to preserve its reporting rules while moving legacy data into an analytics-ready model. This project is being built in stages so the source data, assumptions, transformation logic, and validation approach are reviewable.

## Current files

- `data/patients_legacy.csv` — 250 synthetic patient records.
- `data/visits_legacy.csv` — 500 synthetic visit records.
- `docs/data_dictionary.md` — row grain, field definitions, and format notes.

All records are fictional and generated for demonstration. They do not represent real patients or a healthcare organization.

## Data grain

- **Patients:** one row per `patient_id`.
- **Visits:** one row per `visit_id`. A patient may have multiple visits.

## Planned project stages

1. Document the source files and business assumptions.
2. Add the legacy reporting query and source-to-target mapping.
3. Define the Snowflake-style target model.
4. Add a local reconciliation example and document its actual output.

## Current limitations

This stage does not include a running transformation, a Snowflake connection, or target-side reconciliation. I’ll update this README as each stage is implemented.

## Repository structure

```text
data/
  patients_legacy.csv
  visits_legacy.csv
docs/
  data_dictionary.md
README.md
