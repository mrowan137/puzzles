-- runtime: 309 ms, faster than 62.26% of mysql online submissions for find the team size.
-- memory usage: 0b, less than 100.00% of mysql online submissions for find the team size.
SELECT 
  employee_id, 
  count(employee_id) OVER(PARTITION BY team_id) as team_size 
FROM 
  employee;
