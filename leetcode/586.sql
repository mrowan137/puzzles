-- Runtime: 432 ms, faster than 79.29% of MySQL online submissions for Customer Placing the Largest Number of Orders.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customer Placing the Largest Number of Orders.
-- get all the numbers
SELECT 
  customer_number 
FROM 
  orders -- collapse the customer numbers and add counts
GROUP BY 
  customer_number -- sort in descending order of 
ORDER BY 
  COUNT(customer_number) DESC 
LIMIT 
  1;
