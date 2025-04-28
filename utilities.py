import sqlite3
import os
import pandas as pd


class DBConnect:
    def __init__(self):
        have_db = os.path.exists("relics.db")

        self.connection = sqlite3.connect("relics.db")
        self.cursor = self.connection.cursor()

        if not have_db:
            self.cursor.execute("""
                CREATE TABLE relics(
                    relic_set TEXT,
                    relic_part TEXT,
                    main_stat TEXT,
                    stat_one TEXT,
                    stat_two TEXT,
                    stat_three TEXT,
                    stat_four TEXT,
                    key_one INTEGER,
                    key_two INTEGER,
                    key_three INTEGER,
                    key_four INTEGER
                )
            """)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def add_to_relics(self, relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four, key_one, key_two, key_three, key_four):
        statement = """
            INSERT INTO relics (relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four, key_one, key_two, key_three, key_four)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(statement, (relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four, key_one, key_two, key_three, key_four))
        self.connection.commit()
    
    def remove_from_relics(self, relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four):
        statement = """
            DELETE FROM relics WHERE relic_set = ? AND relic_part = ? AND main_stat = ? AND stat_one = ? AND stat_two = ? AND stat_three = ? AND stat_four = ?
        """
        self.cursor.execute(statement, (relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four))
        self.connection.commit()

    def search_db(self, important_stat, all = False):
        if all:
            res = self.cursor.execute("SELECT relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four FROM relics")
        else:
            res = self.cursor.execute(f"SELECT relic_set, relic_part, main_stat, stat_one, stat_two, stat_three, stat_four FROM relics WHERE {important_stat} = 1")
        rows = res.fetchall()
        print_db_fetch_res(rows)

    def close(self):
        self.cursor.close()
        self.connection.close()

def calc_shift(start, shift):
    after_shift = (start + shift) % 4
    if after_shift == 0:
        after_shift = 4
    return after_shift

def search_csv(important_stat):
    df = pd.read_csv("./relics.csv")
    result = df[df[important_stat] == 1]
    return result.iloc[:, :-4]

def print_db_fetch_res(rows):
    print("Relic Set | Part | Main Stat | Stat One | Stat Two | Stat Three | Stat Four")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]}")
    print("-" * 70)