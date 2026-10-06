# Reporting assumptions

This synthetic portfolio project uses the following rule for its monthly revenue example:

- Only visits with status `Completed` count toward completed visit totals and recognized revenue.
- Visits with status `Cancelled` or `No Show` remain in the source data but are excluded from this specific summary.
- Revenue is grouped by visit month and department.
- These are assumptions invented for this demo, not real healthcare policy.

Before applying a similar rule in a real migration, confirm the definitions with the data owner.
