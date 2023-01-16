-- runtime: 530 ms, faster than 73.48% of mysql online submissions for daily leads and partners.
-- memory usage: 0b, less than 100.00% of mysql online submissions for daily leads and partners.
SELECT 
  date_id, 
  make_name, 
  count(distinct lead_id) as unique_leads, 
  count(distinct partner_id) as unique_partners 
FROM 
  dailysales 
GROUP BY 
  date_id, 
  make_name;
