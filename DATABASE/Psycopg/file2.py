from stringcolor import *
import psycopg2
import time
from getpass import getpass
class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cur = None
    def connect(self, dbname, user, password, host):
        self.conn = psycopg2.connect(f"dbname={dbname} user={user} password='{password}' host={host}")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
    def show_databases(self):
        self.cur.execute("SELECT datname FROM pg_database")
        print("Databases:", self.cur.fetchall())
        time.sleep(2)
    def show_tables(self):
        self.cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
        print("Tables:", self.cur.fetchall())
        time.sleep(2)

    def display_all_rows(self, table_name):
        self.cur.execute(f"SELECT * FROM {table_name}")
        print(f"Data from {table_name}: ", self.cur.fetchall())

    def show_columns(self, table_name):
        self.cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
        return [column[0] for column in self.cur.fetchall()]

    def create_database(self, dbname):
        self.cur.execute(f"CREATE DATABASE {dbname}")
        time.sleep(2)

    def create_table(self, table_name, columns):
        column_str = ', '.join(columns)
        self.cur.execute(f"CREATE TABLE {table_name} ({column_str})")
        self.conn.commit()
        time.sleep(2)

    def delete_table(self, table_name):
        self.cur.execute(f"DROP TABLE {table_name}")
        self.conn.commit()
        time.sleep(2)

    def create_view(self, view_name, query):
        self.cur.execute(f"CREATE VIEW {view_name} AS {query}")
        self.conn.commit()
        time.sleep(2)
    def delete_view(self, view_name):
        self.cur.execute(f"DROP VIEW {view_name}")
        self.conn.commit()
        time.sleep(2)
    def insert_data(self, table_name):
        columns = self.show_columns(table_name)
        if columns:
            values = []
            for column in columns[1:]:  # Skip first column (assuming it's ID)
                value = input(f"Enter value for {column}: ")
                values.append(value)
            columns_str = ', '.join(columns[1:])
            values_str = ', '.join(f"'{value}'" if value else 'NULL' for value in values)
            self.cur.execute(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})")
            self.conn.commit()
            time.sleep(2)

    def close(self):
        self.conn.close()

def main():
    manager = DatabaseManager()
    print(cs("Welcome to the simple DB Manager. What you wanna do?", "yellow"))
    print("1. Connect to a database")
    print("2. Create a new database")
    action = input(cs("Choose an action (1 or 2): ", "yellow"))

    if action == '1':
        manager.connect('postgres', 'postgres', 'doublek', 'localhost')  # Connect to 'postgres' DB
        manager.show_databases()  # Now show databases
        dbname = input("Enter database name: ")  # Then get the database to connect to
        manager.connect(dbname, 'postgres', 'doublek', 'localhost')  # Finally, connect to chosen DB
    else:
        print(cs("Invalid option, homie. Exiting.", "red"))
        retur
    while True:
        print("\nWhat's next?")
        print("1. Create a table")
        print("2. Show tables")
        print("3. Delete table")
        print("4. Insert data into a table")
        print("5. Display all rows from a table")
        print("6. Create a view")
        print("7. Delete a view")
        print("8. Exit")
        action = input(cs("Choose an action: ", "yellow"))

        if action == '1':
            table_name = input("Enter table name: ")
            n_columns = int(input("How many columns?: "))
            columns = []
            for _ in range(n_columns):
                column_name = input("Enter column name: ")
                column_type = input("Enter column type: ")
                columns.append(f"{column_name} {column_type}")
            manager.create_table(table_name, columns)
        elif action == '2':
            manager.show_tables()
        elif action == '3':
            manager.show_tables()
            table_name = input("Enter table name to delete: ")
            manager.delete_table(table_name)
        elif action == '4':
            manager.show_tables()
            table_name = input("Enter table name: ")
            manager.insert_data(table_name)
        elif action == '5':
            table_name = input("Enter table name: ")
            manager.display_all_rows(table_name)
        elif action == '6':
            view_name = input("Enter view name: ")
            query = input("Enter the SQL query for the view: ")
            manager.create_view(view_name, query)
        elif action == '7':
            view_name = input("Enter view name to delete: ")
            manager.delete_view(view_name)
        elif action == '8':
            manager.close()
            print(cs("We out. Peace.", "red"))
            break

if __name__ == "__main__":
    main()