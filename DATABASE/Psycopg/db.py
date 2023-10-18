import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres password='postgres' host=localhost")
conn.autocommit = True

# CREATING DB
cursor = conn.cursor()
cursor.execute("CREATE DATABASE music")
conn.close()

# Connecting to it
conn = psycopg2.connect("dbname=music user=postgres password='postgres' host=localhost")
cursor = conn.cursor()


# Creating the table musicians
cursor.execute("""
    CREATE TABLE musicians (
        first_name VARCHAR(40),
        last_name VARCHAR(40),
        date_of_birth TIMESTAMP,
        instrument varchar(100)
    );
""")
conn.commit()


# Adding values to the table
cursor.execute("""
    INSERT INTO musicians (first_name, last_name, date_of_birth, instrument) VALUES
    ('Justin', 'Bieber', '1994-03-01 00:00:00', 'Voice'),
    ('Lady', 'Gaga', '1986-03-28 00:00:00', 'Voice'),
    ('Alejandro', 'Sanz', '1968-12-18 00:00:00', 'Voice'),
    ('Jimmy', 'Hendrix', '1942-11-27 00:00:00', 'Guitar'),
    ('Charlie', 'Parker', '1920-08-29 00:00:00', 'Saxophone');

""")
conn.commit()

# Showing a list of musicians sorted by date of birth.
cursor.execute("SELECT * FROM musicians ORDER BY date_of_birth;")
print("Musicians:", cursor.fetchall())


# Deleting the musicians 
cursor.execute("""
    DELETE FROM musicians 
    WHERE first_name IN ('Justin' , 'Lady', 'Alejandro', 'Jimmy', 'Charlie');
""")
conn.commit()


# Changing Saxphone to Saxophone
cursor.execute("""
    UPDATE public.musicians SET instrument = 'Saxophone' 
    WHERE instrument = 'Saxphone';
""")
conn.commit()

# Close the connection
conn.close()