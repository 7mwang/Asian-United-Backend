import sqlite3
import os
# Get the absolute path to the 'instance' directory
instance_directory = os.path.abspath('instance')

# Specify the absolute path to the database file
db_file_path = os.path.join(instance_directory, 'volumes', 'scores.db')

# Connect to the database using the absolute path
conn = sqlite3.connect(db_file_path)
# Connect to the database
cursor = conn.cursor()

# Execute a query to fetch and print all records from the game_scores table
cursor.execute('SELECT * FROM game_scores')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Execute a query to fetch and print all records from the user_data table
cursor.execute('SELECT * FROM user_data')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
