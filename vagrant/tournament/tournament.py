#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) as number_of_players FROM players")
    players_count = c.fetchone()[0]
    DB.close()
    return players_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("insert into players(name , matches_played) values (%s,0)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    c = DB.cursor()
    c.execute(
        """select players.id, players.name, count(matches.winner_id) as wins, players.matches_played
        from players left outer join matches
        on matches.winner_id = players.id
        group by players.id , players.name
        order by wins desc;
        """)
    players_record = c.fetchall()
    DB.close()
    return players_record


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute(
        "insert into matches(winner_id , loser_id) values (%s, %s) returning id ;",
        (winner,
         loser,
         ))
    match_id = c.fetchone()[0]
    c.execute(
        "select  winner_id , loser_id from matches where id = %s ;", (match_id,))
    match_players = c.fetchall()
    c.execute(
        "update players set matches_played = matches_played + 1 where id = %s or id = %s ;",
        (match_players[0][0],
         match_players[0][1],
         ))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    swiss_pairs = []
    ranking = []
    r = playerStandings()
    for row in r:
        ranking.append(row)

    swiss_pairs = []
    while len(ranking) > 1:
        p1 = ranking.pop(0)
        p2 = ranking.pop(0)
        swiss_pairs.append((p1[0], p1[1], p2[0], p2[1]))

    return swiss_pairs
