-- Runtime: 1530 ms (Beats 25.87%)
SELECT 
  id, 
  name 
FROM 
  Students 
WHERE 
  department_id NOT IN (
    SELECT 
      id 
    FROM 
      Departments
  )
