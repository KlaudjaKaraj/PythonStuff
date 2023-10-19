import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            database="music",
            user="postgres",
            password="doublek",
            host="localhost",
            port=5432,
        )
    except psycopg2.Error as e:
        print(f"Could not connect! {e}")
        return False
 
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
 
# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM musicians;")
 
# FETCH ALL THE ROWS FROM THE CURSOR
#data = curr.fetchall()
# for row in data:
#     print(row)


 # FETCH THE FIRST ROW FROM THE CURSOR
# data1 = curr.fetchone()
# print(data1)
 
# FETCH THE SECOND ROW FROM THE CURSOR
# data2 = curr.fetchone()
# print(data2)
 # PRINT THE RECORDS




# GET FIRST TWO RECORDS FROM DATABASE TABLE
data1 = curr.fetchmany(2)
for row in data1:
    print(row)
 
print("Next three records:")
 
# GET NEXT THREE RECORDS FROM DATABASE TABLE
data2 = curr.fetchmany(3)
for row in data2:
    print(row)
 
# CLOSE THE CONNECTION
conn.close()
 
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")