-- runtime: 680 ms, faster than 72.55% of mysql online submissions for find customers with positive revenue this year.
-- memory usage: 0b, less than 100.00% of mysql online submissions for find customers with positive revenue this year.
SELECT 
  customer_id 
FROM 
  customers 
WHERE 
  revenue > 0 
  and year = 2021;
