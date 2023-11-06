import sqlite3
import os
# Get the absolute path to the 'instance' directory
instance_directory = os.path.abspath('instance')

# Specify the absolute path to the database file
db_file_path = os.path.join(instance_directory, 'volumes', 'scores.db')

# Connect to the database using the absolute path
conn = sqlite3.connect(db_file_path)

cursor = conn.cursor()
print("this works")
# Create a table for game scores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS game_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        score INTEGER NOT NULL
    )
''')

# Create a table for user data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        user_id TEXT PRIMARY KEY,
        count INTEGER,
        rate REAL,
        cost INTEGER,
        clickerCost INTEGER,
        clickerCount INTEGER,
        doubleCount INTEGER,
        dbCost INTEGER,
        plusCount INTEGER
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
