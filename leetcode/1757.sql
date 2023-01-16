-- runtime: 418 ms, faster than 90.66% of mysql online submissions for recyclable and low fat products.
-- memory usage: 0b, less than 100.00% of mysql online submissions for recyclable and low fat products.
SELECT 
  product_id 
FROM 
  products 
WHERE 
  low_fats = 'Y' 
  and recyclable = 'Y';
