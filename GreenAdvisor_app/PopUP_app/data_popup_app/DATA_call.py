import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/Users/panpom/PycharmProjects/GreenGrow_Advisor/Database/Main_data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Example data to insert
new_data = [
    ('P_005', 'x3', 'new_value', 5),
    ('P_006', 'x4', 'another_value', 8)
]

# Insert data into the Main_data table
cursor.executemany("INSERT INTO Main_data VALUES (?, ?, ?, ?)", new_data)

# Commit the changes
conn.commit()

# Fetch and display the updated data to confirm the insertion
cursor.execute("SELECT * FROM Main_data")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
