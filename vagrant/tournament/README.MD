Project 2 - Tournament Results version 1.0 25/04/2016

Description
-----------------

This project is a python module that uses the PostgreSQL database to keep track
of players and matches in a game tournament, and ranks and pairs matches using
swiss pairing scheme.

What's included
-----------------
The following files are included in the project:
├── tournament.py
├── tournament_test.py
├── tournament.sql

tournament.sql contains the sql create table statements.
tournament.py contains the project implementation.
tournament_test.py contains the code to test tournament.py

Running the code
-----------------
Make sure that you have Python 2.7 and PostgreSQL 9.1 or later installed 
on your computer.

On a mac or linux, open terminal, and navigate to where you downloaded
the project files, then:
1) Type psql to connect to PostgreSQL
2) From the psql command line interface, type: CREATE DATABASE tournament; 
   This will create the database called tournament.
3) Type: \c tournament;
   This will connect to the created database in step 2
4) Type: \i tournament.sql
   This will execute the create table sql statements we have in our tournament.sql file
5) Next, exist the psql CLI, through typing \q
6) From the terminal shell type the following to execute the tournament test code. 
>python tournament_test.py

On windows, Go to Start->run ->  type cmd  <press enter>
Then from the command prompt type:
1) psql -U postgres template1
   This will connect to PostgreSQL
2) From the psql command line interface, type: CREATE DATABASE tournament;
   This will create the database called tournament.
3) Type: \c tournament;
   This will connect to the created database in step 2
4) Type: \i tournament.sql
   This will execute the create table sql statements we have in our tournament.sql file
5) Next, exist the psql CLI, through typing \q 
6) Open the file tournament_test.py in IDLE, and make sure that
all the downloaded files are in the same directory, and then select:
Run > Run Module

A successful run results in:
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!

Creator
------------------
Elie Shalhoub
