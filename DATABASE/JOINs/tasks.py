import psycopg2


def connect_to_postgres():
    try:
        return psycopg2.connect(
            database="postgres",
            user="postgres",
            password="doublek",
            host="localhost",
            port=5432,
        )
    except psycopg2.Error as e:
        print(f"Failed to connect to postgres {e}")
        return None


# 2 create database
def create_shop_database():
    conn = connect_to_postgres()
    conn.autocommit = True  # enable autocommit for db
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE shop")
            conn.close()
        except psycopg2.Error as e:
            print(f"Error creating or checking the database: {e}")


# Connecting to the database
def connecting_to_shop_db():
    try:
        return psycopg2.connect(
            database="shop",
            user="postgres",
            password="doublek",
            host="localhost",
            port=5432,
        )
    except psycopg2.Error as err:
        print(f"Error connecting to the shop database {err}")
        return None


def create_clients_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE clients (
            client_id SERIAL PRIMARY KEY,
            client_name VARCHAR(100),
            email VARCHAR(100));
        """
        )
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print(f"Failed to create the table {e}")


def create_products_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(100),
            price NUMERIC(10, 2), -- Add a price column
            client_id INT);
        """
        )
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print(f"Failed to create the product table {e}")


def insering_values_to_client_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO clients (client_name, email)
            VALUES
            ('Client A', 'clientA@example.com'),
            ('Client B', 'clientB@example.com'),
            ('Client C', 'clientC@example.com'),
            ('Client D', 'clientD@example.com'),
            ('Client E', 'clientE@example.com'),
            ('Client F', 'clientF@example.com'),
            ('Client X', 'clientX@example.com');
        """
        )
        conn.commit()
        cursor.close()
    except psycopg2.Error as err:
        print(f"Could not insert the values to cilent table! {err}")


def inserting_values_to_product_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO products (product_name, price, client_id)
            VALUES
            ('Product X', 19.99, 1),  -- Belongs to Client A
            ('Product Y', 29.99, 1),  -- Belongs to Client A
            ('Product Z', 49.99, 2),  -- Belongs to Client B
            ('Product W', 15.99, 3),  -- Belongs to Client C
            ('Product Q', 14.50, 3),  -- Belongs to Client C
            ('Product M', 34.99, 4),  -- Belongs to Client D
            ('Product N', 25.00, 5),  -- Belongs to Client E
            ('Product P', 17.99, 5),  -- Belongs to Client E
            ('Product R', 21.50, 1),  -- Belongs to Client A
            ('Product S', 39.99, 2),  -- Belongs to Client B
            ('Product T', 12.95, 3),  -- Belongs to Client C
            ('Product U', 29.95, 3),  -- Belongs to Client C
            ('Product V', 9.99, 3),   -- Belongs to Client C
            ('Product X', 17.50, 4),  -- Belongs to Client D
            ('Product Y', 23.95, 5),  -- Belongs to Client E
            ('Product Z', 31.99, 1),  -- Belongs to Client A
            ('Product W', 22.00, 2),  -- Belongs to Client B
            ('Product Q', 13.75, 2),  -- Belongs to Client B
            ('Product M', 27.50, 3),  -- Belongs to Client C
            ('Product N', 18.99, 4),
            ('Product A', 19.99, null),  -- Belongs to Client A
            ('Product B', 29.99, null),  -- Belongs to Client A
            ('Product C', 49.99, null);
        """
        )
        conn.commit()
        cursor.close()
    except psycopg2.Error as err:
        print(f"Could not insert the values to product table! {err}")
        return None


def get_inner_join(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT clients.client_name, products.product_name
            FROM clients
            INNER JOIN products 
            ON clients.client_id = products.client_id;
        """
        )
        conn.commit()

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
    except psycopg2.Error as err:
        print(f"Could not get inner join! {err}")
        return None


def get_left_join(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT clients.client_name,products.product_name               
            FROM clients 
            LEFT JOIN products 
            ON clients.client_id = products.client_id where products.price > 20;
        """
        )
        conn.commit()
        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
    except psycopg2.Error as err:
        print(f"Could not get left join! {err}")
        return None


def get_right_join(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT clients.client_name,products.product_name
            FROM clients
            RIGHT JOIN products
            ON clients.client_id = products.client_id order by clients.client_name;
        """
        )
        conn.commit()
        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
    except psycopg2.Error as err:
        print(f"Could not get left join! {err}")
        return None


if __name__ == "__main__":
    create_shop_database()

    # Connect to the shop database
    conn = connecting_to_shop_db()
    create_clients_table(conn)

    insering_values_to_client_table(conn)

    create_products_table(conn)

    inserting_values_to_product_table(conn)

    # Connect  to perform joins
    conn = connecting_to_shop_db()

    print("Inner Join:")
    get_inner_join(conn)

    print("\nLeft Join:")
    get_left_join(conn)

    print("\nRight Join:")
    get_right_join(conn)

    # Close the connection
    conn.close()
