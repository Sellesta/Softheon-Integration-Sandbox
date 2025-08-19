-- Fetch active members from the Softheon staging table
SELECT 
    member_id,
    first_name,
    last_name,
    date_of_birth,
    plan_id,
    enrollment_date
FROM softheon_staging.members
WHERE is_active = 1
ORDER BY enrollment_date DESC
LIMIT 100;
