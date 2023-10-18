from stringcolor import *
import psycopg2
import time

# green for creation
# violet for fetching
# blue for updates
# red for deletion

# Connect to the postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password='doublek' host=localhost")
conn.autocommit = True

# Open a cursor to perform database operations
cur = conn.cursor()

# Create a new database
print(cs("Creating database...", "green"))
cur.execute("CREATE DATABASE mydatabase")
time.sleep(2)

input("PRESS ENTER TO CREATE AND INSERT")

# Close the current connection and connect to the new database
conn.close()
conn = psycopg2.connect("dbname=mydatabase user=postgres password='doublek' host=localhost")
cur = conn.cursor()

# Create a table 'crimes'
print(cs("Creating table 'crimes'...", "green"))
cur.execute("""
    CREATE TABLE crimes (
        id SERIAL PRIMARY KEY,
        type VARCHAR(50),
        description TEXT,
        is_solved BOOLEAN
    )
""")
conn.commit()
time.sleep(2)

# Insert data into 'crimes' table
print(cs("Inserting data into 'crimes' table...", "green"))
cur.execute("""
    INSERT INTO crimes (type, description, is_solved) 
    VALUES ('Theft', 'A bike was stolen from the city center.', false)
""")
conn.commit()
time.sleep(2)

# Create a table 'officers'
print(cs("Creating table 'officers'...", "green"))
cur.execute("""
    CREATE TABLE officers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        rank VARCHAR(50),
        crime_id INTEGER,
        FOREIGN KEY (crime_id) REFERENCES crimes(id)
    )
""")
conn.commit()
time.sleep(2)

# Insert data into 'officers' table
print(cs("Inserting data into 'officers' table...", "green"))
cur.execute("""
    INSERT INTO officers (name, rank, crime_id) 
    VALUES ('John Doe', 'Detective', 1)
""")
conn.commit()
time.sleep(2)

input("PRESS ENTER TO FETCH")

# Fetch and display data from both tables using fetchall()
print(cs("Fetching data from both tables using fetchall()...", "magenta"))
cur.execute("SELECT * FROM crimes")
print("Crimes:", cur.fetchall())
cur.execute("SELECT * FROM officers")
print("Officers:", cur.fetchall())
time.sleep(2)

# Show the use of fetchone()
print(cs("Fetching a single record using fetchone()...", "magenta"))
cur.execute("SELECT * FROM crimes WHERE id = 1")
print("Crime:", cur.fetchone())
time.sleep(2)

input("PRESS ENTER FOR VIEWS")

# Create a view to show unsolved crimes
print(cs("Creating a view for unsolved crimes...", "green"))
cur.execute("""
    CREATE VIEW unsolved_crimes AS
    SELECT * FROM crimes WHERE is_solved = false
""")
conn.commit()
time.sleep(2)

# Create a view to show officers working on unsolved crimes
print(cs("Creating a view for officers working on unsolved crimes...", "green"))
cur.execute("""
    CREATE VIEW officers_unsolved AS
    SELECT o.* FROM officers o
    INNER JOIN crimes c ON o.crime_id = c.id
    WHERE c.is_solved = false
""")
conn.commit()
time.sleep(2)

input("PRESS ENTER TO QUERY VIEWS")

# Query the views and display the results
print(cs("Fetching data from unsolved_crimes view...", "magenta"))
cur.execute("SELECT * FROM unsolved_crimes")
print("Unsolved Crimes:", cur.fetchall())
time.sleep(2)

print(cs("Fetching data from officers_unsolved view...", "magenta"))
cur.execute("SELECT * FROM officers_unsolved")
print("Officers on Unsolved Crimes:", cur.fetchall())
time.sleep(2)

input("PRESS ENTER FOR UPDATES")

# Update data in 'crimes' table
print(cs("Updating data in 'crimes' table...", "blue"))
cur.execute("UPDATE crimes SET is_solved = true WHERE id = 1")
conn.commit()
time.sleep(2)

# Fetch and display updated data from 'crimes' table
print(cs("Fetching updated data from 'crimes' table...", "magenta"))
cur.execute("SELECT * FROM crimes")
print("Crimes:", cur.fetchall())
time.sleep(2)

input("PRESS ENTER FOR DELETIONS")

# Delete data from 'officers' table
print(cs("Deleting data from 'officers' table...", "red"))
cur.execute("DELETE FROM officers WHERE id = 1")
conn.commit()
time.sleep(2)

# Delete data from 'crimes' table
print(cs("Deleting data from 'crimes' table...", "red"))
cur.execute("DELETE FROM crimes WHERE id = 1")
conn.commit()
time.sleep(2)

input("PRESS ENTER TO DROP")

# Drop tables and views
print(cs("Dropping tables and views...", "red"))
cur.execute("DROP VIEW officers_unsolved")
cur.execute("DROP VIEW unsolved_crimes")
cur.execute("DROP TABLE officers")
cur.execute("DROP TABLE crimes")
conn.commit()
time.sleep(2)

# Close the current connection and connect to the default database
conn.close()
conn = psycopg2.connect("dbname=postgres user=postgres password='doublek' host=localhost")
conn.autocommit = True
cur = conn.cursor()

# Drop the database
print(cs("Dropping database...", "red"))
cur.execute("DROP DATABASE mydatabase")
time.sleep(2)

# Close the connection
conn.close()
print(cs("DONE DONE DONE", "yellow"))