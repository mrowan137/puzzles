-- Runtime: 403 ms, faster than 21.15% of MySQL online submissions for Big Countries.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Big Countries.
SELECT 
  name, 
  population, 
  area 
FROM 
  World 
WHERE 
  area >= 3e6 
  OR population >= 25000000
