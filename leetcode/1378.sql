-- runtime: 1560 ms, faster than 40.07% of mysql online submissions for replace employee id with the unique identifier.
-- memory usage: 0b, less than 100.00% of mysql online submissions for replace employee id with the unique identifier.
SELECT 
  euni.unique_id, 
  e.name 
FROM 
  employees e 
  LEFT JOIN employeeuni euni ON e.id = euni.id;
