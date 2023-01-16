-- runtime: 545 ms, faster than 25.05% of mysql online submissions for apples & oranges.
-- memory usage: 0b, less than 100.00% of mysql online submissions for apples & oranges.
SELECT 
  sale_date, 
  sum(
    case when fruit = 'apples' then + sold_num else - sold_num end
  ) as diff 
FROM 
  sales 
GROUP BY 
  sale_date;
