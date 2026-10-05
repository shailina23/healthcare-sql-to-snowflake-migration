-- Legacy-style reporting query.
-- Business rule: only completed visits count toward recognized revenue.
SELECT
    substr(v.visit_date, 1, 7) AS revenue_month,
    v.department,
    COUNT(*) AS completed_visits,
    ROUND(SUM(v.billed_amount), 2) AS recognized_revenue
FROM visits v
WHERE v.status = 'Completed'
GROUP BY substr(v.visit_date, 1, 7), v.department
ORDER BY revenue_month, department;
