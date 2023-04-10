SELECT
  game_id,
  season,
  player_id,
  first_name,
  last_name,
  team_id,
  name as team,
  position,
  points,
  rebounds,
  assists,
  turnovers
FROM
   {{ ref('mbb_players_games_sr') }} 
  
  inner join  {{ ref('mbb_teams') }} 
  on team_id=id