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
  `de-trainig.de_project.mbb_players_games_sr` as p
  inner join `de_project.mbb_teams` as t on team_id=id