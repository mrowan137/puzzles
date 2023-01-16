-- runtime: 351 ms, faster than 83.07% of mysql online submissions for combine two tables.
-- memory usage: 0b, less than 100.00% of mysql online submissions for combine two tables.
SELECT 
  firstname, 
  lastname, 
  city, 
  state 
FROM 
  person 
  LEFT JOIN address ON person.personid = address.personid;
