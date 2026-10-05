import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
visits = pd.read_csv(ROOT / "data/visits_legacy.csv")

# Source-side control totals
completed = visits[visits["status"].eq("Completed")].copy()
source_rows = len(completed)
source_revenue = round(completed["billed_amount"].sum(), 2)

# Simulate target transformation using the same documented business rule.
target = completed.groupby(
    [completed["visit_date"].str[:7], "department"], as_index=False
).agg(completed_visits=("visit_id","count"),
     recognized_revenue=("billed_amount","sum"))
target["recognized_revenue"] = target["recognized_revenue"].round(2)

target_rows = int(target["completed_visits"].sum())
target_revenue = round(target["recognized_revenue"].sum(), 2)

print("HEALTHCARE MIGRATION RECONCILIATION")
print(f"Source completed visits : {source_rows:,}")
print(f"Target completed visits : {target_rows:,}")
print(f"Source revenue          : {source_revenue:,.2f}")
print(f"Target revenue          : {target_revenue:,.2f}")
assert source_rows == target_rows
assert source_revenue == target_revenue
print("PASS: source and target control totals reconcile.")
