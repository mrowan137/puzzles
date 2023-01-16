-- runtime: 953 ms, faster than 22.06% of mysql online submissions for all the matches of the league.
-- memory usage: 0b, less than 100.00% of mysql online submissions for all the matches of the league.
SELECT 
  t_away.team_name as home_team, 
  t_home.team_name as away_team 
FROM 
  teams t_away 
  join teams t_home ON t_away.team_name != t_home.team_name;
