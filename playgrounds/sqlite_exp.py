import sqlite3



# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Insert some data
# cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
# cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))

# Commit the transaction
conn.commit()

# Execute a SELECT query
cursor.execute('SELECT * FROM users')

# Fetch all rows from the result
rows = cursor.fetchall()

# Iterate over the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
