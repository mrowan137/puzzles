-- runtime: 493 ms, faster than 87.57% of mysql online submissions for number of unique subjects taught by each teacher.
-- memory usage: 0b, less than 100.00% of mysql online submissions for number of unique subjects taught by each teacher.
SELECT 
  teacher_id, 
  count(distinct subject_id) as cnt 
FROM 
  teacher 
GROUP BY 
  teacher_id;
