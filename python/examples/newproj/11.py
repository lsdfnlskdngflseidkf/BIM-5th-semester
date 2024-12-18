import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("student.db")
cur = connection.cursor()

# Create the table if it does not exist
create = """CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT
            )"""
cur.execute(create)

# Insert sample data into the table
ins = """INSERT INTO student (name, age, gender) 
         VALUES ('Ujwal', 20, 'male'),
                ('ronish', 20, 'male'),
                ('khusi', 20, 'female')"""
cur.execute(ins)

# Select records where gender is 'male'
ret = """SELECT * FROM student WHERE gender = 'male'"""
data = cur.execute(ret).fetchall()

# Print the results
for i in data:
    print(i)

# Commit changes and close the connection
connection.commit()
connection.close()
