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
  `de-trainig.de_project.mbb_teams` AS teams
INNER JOIN
  `de-trainig.de_project.mbb_teams_games_sr` AS games
ON
  teams.id = games.team_id

