-- Runtime: 468 ms, faster than 75.09% of MySQL online submissions for Find Total Time Spent by Each Employee.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Find Total Time Spent by Each Employee.
-- Compute: time spent by each employee on each day at office
-- emp_id | day_at_office | time_at_office
-- 1) compute time at office per employee per day
-- 2) sum of the times at office per employee per day
SELECT 
  e.emp_id, 
  e.event_day as day, 
  sum(e.out_time - e.in_time) as total_time 
FROM 
  employees e 
GROUP BY 
  day, 
  emp_id;
