# pitchfork.py

import sqlite3
from player import Player
from token import Token

class Pitchfork:
    def __init__(self):
        self.conn = sqlite3.connect("pitchfork.db")
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS players (
                name TEXT PRIMARY KEY,
                red INTEGER,
                orange INTEGER,
                yellow INTEGER,
                green INTEGER,
                blue INTEGER,
                purple INTEGER,
                skills INTEGER,
                contracts INTEGER
            )
        ''')
        self.conn.commit()

    def create_player(self, name):
        self.conn.execute(
            '''
            INSERT INTO players (name, red, orange, yellow, green, blue, purple, skills, contracts)
            VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0)
            ''',
            (name,)
        )
        self.conn.commit()

    def get_player(self, name):
        cursor = self.conn.execute(
            "SELECT red, orange, yellow, green, blue, purple, skills, contracts FROM players WHERE name = ?",
            (name,)
        )
        row = cursor.fetchone()
        if row:
            tokens = {color: row[i] for i, color in enumerate(Token.COLORS)}
            progress = {"skills": row[6], "contracts": row[7]}
            return Player(name, tokens, progress)
        return None

    def get_player_tokens(self, name):
        player = self.get_player(name)
        if player:
            return player.get_tokens()
        return None

    def collect_player_token(self, name, color):
        if self.player_exists(name):
            if color in Token.COLORS:
                player = self.get_player(name)
                if player.collect_token(color):  # Pass color to collect_token method
                    self.update_database(name, color, player.tokens[color])  # Update the database with new token count
                    self.update_database(name, "skills", player.progress["skills"])  # Update the database with skill progress
                    return True
        return False

    def get_player_progress(self, name):
        player = self.get_player(name)
        if player:
            return player.get_progress()
        return None

    def get_all_players(self):
        cursor = self.conn.execute("SELECT name FROM players")
        players = [row[0] for row in cursor.fetchall()]
        return players

    def player_exists(self, name):
        cursor = self.conn.execute("SELECT name FROM players WHERE name = ?", (name,))
        return cursor.fetchone() is not None

    def update_database(self, player_name, column, value):
        self.conn.execute(
            f"UPDATE players SET {column} = ? WHERE name = ?",
            (value, player_name)
        )
        self.conn.commit()
