-- Runtime: 1272 ms, faster than 7.22% of MySQL online submissions for Rearrange Products Table.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rearrange Products Table.
-- Given:
--   Products gives product_id: id
--                  store1    : price
--                  store2    : price
--                  store3    : price
-- Goal:
--   Create single tables of rows of (product_id, store, price)
--
WITH product_store_price AS (
  SELECT 
    product_id, 
    "store1" AS store, 
    store1 AS price 
  FROM 
    products 
  UNION 
  SELECT 
    product_id, 
    "store2" AS store, 
    store2 AS price 
  FROM 
    products 
  UNION 
  SELECT 
    product_id, 
    "store3" AS store, 
    store3 AS price 
  FROM 
    products
) 
SELECT 
  * 
FROM 
  product_store_price 
WHERE 
  price IS NOT NULL
