-- runtime: 693 ms, faster than 44.57% of mysql online submissions for capital gain/loss.
-- memory usage: 0b, less than 100.00% of mysql online submissions for capital gain/loss.
SELECT 
  stock_name, 
  sum(
    case when operation = 'Buy' then - price else + price end
  ) as capital_gain_loss 
FROM 
  stocks 
GROUP BY 
  stock_name;
