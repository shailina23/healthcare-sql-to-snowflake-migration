# Migration mapping

| Legacy field | Target field | Rule |
|---|---|---|
| patients.patient_id | RAW.PATIENTS.PATIENT_ID | direct |
| patients.dob | RAW.PATIENTS.DOB | cast to DATE |
| visits.visit_id | RAW.VISITS.VISIT_ID | direct |
| visits.visit_date | RAW.VISITS.VISIT_DATE | cast to DATE |
| visits.billed_amount | RAW.VISITS.BILLED_AMOUNT | numeric(12,2) |
| visits.status | RAW.VISITS.STATUS | standardized status |

## Validation
1. Row counts by source table.
2. Completed visit count.
3. Recognized revenue total.
4. Monthly + department reconciliation.
5. Null checks on primary/business keys.
