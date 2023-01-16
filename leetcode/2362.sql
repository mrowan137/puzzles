-- Runtime: 1483 ms, faster than 16.60% of MySQL online submissions for Generate the Invoice.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Generate the Invoice.
-- Table of (invoice, total_price)
with sorted as (
  SELECT 
    invoice_id, 
    SUM(quantity * price) as total_price 
  FROM 
    Purchases purchases 
    LEFT JOIN Products products ON purchases.product_id = products.product_id 
  GROUP BY 
    invoice_id 
  ORDER BY 
    total_price DESC, 
    invoice_id ASC 
  LIMIT 
    1
) # Select rows that match the highet price invoice, with lowest invoice id
SELECT 
  purchases.product_id, 
  purchases.quantity, 
  purchases.quantity * products.price as price 
FROM 
  Purchases purchases 
  LEFT JOIN Products products ON purchases.product_id = products.product_id 
WHERE 
  invoice_id = (
    SELECT 
      invoice_id 
    FROM 
      sorted
  )
