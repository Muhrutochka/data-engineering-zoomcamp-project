{{ config(materialized='view') }}

SELECT
  teams.name as team,
  season,
  game_id,
  win, 
  points_game,
  rebounds,
  assists,
  turnovers,
  win
FROM
  {{ ref('mbb_teams_games_sr') }} as games 

  inner join  {{ ref('mbb_teams') }} 
  on team_id=id


