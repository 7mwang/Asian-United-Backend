import sqlite3

# Connect to the database (create a new one if it doesn't exist)
import os
# Get the absolute path to the 'instance' directory
instance_directory = os.path.abspath('instance')

# Specify the absolute path to the database file
db_file_path = os.path.join(instance_directory, 'volumes', 'login.db')

# Connect to the database using the absolute path
conn = sqlite3.connect(db_file_path)

cursor = conn.cursor()

# Create a table for user login data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
