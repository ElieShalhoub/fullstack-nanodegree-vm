-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Create the table for players
Create table players (
	id serial primary key,
	name text
	)

-- Create the matches table
Create table matches (
	id serial primary key,
	player1_id integer references players(id),
	player2_id integer references players(id),
	match_winner integer references players(id)
	)
