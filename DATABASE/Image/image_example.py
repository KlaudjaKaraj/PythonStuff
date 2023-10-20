import psycopg2
from PIL import Image
from io import BytesIO

db_params = {
    "database": "albums",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
}


conn = psycopg2.connect(**db_params)

cur =conn.cursor()

with open('some_image.jpeg','rb') as image_file :
    image_binary = image_file.read()
    

cur.execute("""CREATE TABLE IF NOT EXISTS image_storage (
    id serial PRIMARY KEY,
    image_data bytea
);
""")

conn.commit()
cur.execute(
    "INSERT INTO image_storage (image_data) VALUES (%s)",
    (psycopg2.Binary(image_binary),),
)
conn.commit()

cur.execute("SELECT image_data FROM image_storage WHERE id = 1")
image_binary = cur.fetchone()[0]

cur.close()
conn.close()

image = Image.open(BytesIO(image_binary))
image.show()