-- runtime: 676 ms, faster than 60.45% of mysql online submissions for invalid tweets.
-- memory usage: 0b, less than 100.00% of mysql online submissions for invalid tweets.
SELECT 
  tweet_id 
FROM 
  tweets 
WHERE 
  char_length(content) > 15;
