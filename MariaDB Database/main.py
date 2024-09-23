import pymysql
import os
from dotenv import load_dotenv
from contextlib import closing, contextmanager

# Load environment variables
load_dotenv()

# Retrieve database credentials from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')

class DatabaseManagement:
    """
    A class to manage MySQL/MariaDB databases and tables.
    """

    def __init__(self):
        """
        Initialize DatabaseManagement class with None attributes for engine and connection.
        """
        self.connection = None

    @contextmanager
    def manage_connection(self):
        """
        Context manager to handle database connections.
        Yields:
            pymysql.connections.Connection: A pymysql connection object.
        """
        conn = None
        try:
            conn = pymysql.connect(host=db_host, user=db_user, password=db_password)
            yield conn
        finally:
            if conn:
                conn.close()

    def connect_engine(self):
        """
        Establishes a connection to the database using pymysql.

        Args:
            timeout_seconds (int): Timeout duration in seconds for the connection attempt.

        Returns:
            str: "Pass" if connection is successful, "Fail" if unsuccessful.
        """
        print("\nEstablishing connection: ")
        try:
            self.connection = pymysql.connect(host=db_host, user=db_user, password=db_password)
            print("Connection established successfully.")
            return "Pass"
        except pymysql.MySQLError as e:
            print(f"Error trying to connect to the database: {e}")
            return "Fail"

    def check_database(self, db_name):
        """
        Checks if a database exists with the given name.

        Args:
            db_name (str): The name of the database to check.

        Returns:
            tuple or None: A tuple representing the database if found, None if not found.
        """
        with self.manage_connection() as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SHOW DATABASES LIKE %s", (db_name,))
                return cursor.fetchone()

    def create_database(self, db_name):
        """
        Creates a new database if it does not already exist.

        Args:
            db_name (str): The name of the database to create.

        Returns:
            str: "Pass" if database creation is successful, "Fail" if unsuccessful.
        """
        print("\nCreating database:")
        with self.manage_connection() as conn:
            try:
                db_exists = self.check_database(db_name)
                if db_exists:
                    print(f"The database '{db_name}' already exists.")
                else:
                    with closing(conn.cursor()) as cursor:
                        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                    print(f"Database '{db_name}' created successfully.")
                    print(self.check_database(db_name)[0])
                return self.check_database(db_name)[0]
            except pymysql.MySQLError as e:
                print(f"Error creating database: {e}")
                return "Fail"

    def check_table_exist(self, db_name, table_name):
        """
        Checks if a table exists in the specified database.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to check.

        Returns:
            tuple or None: A tuple representing the table if found, None if not found.
        """
        with self.manage_connection() as conn:
            db_exists = self.check_database(db_name)
            if db_exists:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(f"USE {db_name}")
                    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
                    return cursor.fetchone()
            else:
                print(f"The database '{db_name}' does not exist.")
                return None

    def create_table(self, db_name, table_name, columns):
        """
        Creates a new table in the specified database.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to create.
            columns (dict): A dictionary where keys are column names and values are column types.

        Returns:
            str: "Pass" if table creation is successful, "Fail" if unsuccessful.
        """
        print("\nCreating table:")
        with self.manage_connection() as conn:
            try:
                table_exist = self.check_table_exist(db_name, table_name)
                if table_exist:
                    print(f"Table '{table_name}' already exists.")
                else:
                    columns_definition = ', '.join([f"{name} {type}" for name, type in columns.items()])
                    create_table_query = f"CREATE TABLE {table_name} ({columns_definition})"
                    with closing(conn.cursor()) as cursor:
                        cursor.execute(f"USE {db_name}")
                        cursor.execute(create_table_query)
                    print(f"Table '{table_name}' created successfully.")
                return self.check_table_exist(db_name, table_name)[0]
            except pymysql.MySQLError as e:
                print(f"Error creating table: {e}")
                return "Fail"

    def create_register(self, db_name, table_name, registers):
        """
        Inserts a record into the specified table.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to insert into.
            registers (dict): A dictionary where keys are column names and values are column values.

        Returns:
            str: "Pass" if record insertion is successful, "Fail" if unsuccessful.
        """
        with self.manage_connection() as conn:
            try:
                table_exist = self.check_table_exist(db_name, table_name)
                if table_exist:
                    with closing(conn.cursor()) as cursor:
                        cursor.execute(f"USE {db_name}")
                        columns = ', '.join(registers.keys())
                        placeholders = ', '.join(['%s'] * len(registers))
                        values = tuple(registers.values())
                        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                        cursor.execute(insert_query, values)
                        conn.commit()
                    print(f"Record inserted into table '{table_name}'.")
                    return "Pass"
                else:
                    print(f"The table '{table_name}' does not exist.")
                    return "Fail"
            except pymysql.MySQLError as e:
                print(f"Error inserting into table: {e}")
                return "Fail"

    def get_columns(self, db_name, table_name):
        """
        Retrieves column names from the specified table.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to retrieve columns from.

        Returns:
            list or None: A list of column names if successful, None if unsuccessful.
        """
        with self.manage_connection() as conn:
            try:
                with closing(conn.cursor()) as cursor:
                    cursor.execute(f"USE {db_name}")
                    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                    return [column[0] for column in cursor.fetchall()]
            except pymysql.MySQLError as e:
                print(f"Error getting columns: {e}")
                return None

    def query_data(self, db_name, table_name, filters=None, value=None):
        """
        Queries data from the specified table.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to query.
            filters (dict): A dictionary where keys are column names and values are filter values.
            value (str): A value to search for across all columns using LIKE operator.

        Returns:
            str: "Pass" if data retrieval is successful, "Fail" if unsuccessful.
        """
        with self.manage_connection() as conn:
            try:
                table_exist = self.check_table_exist(db_name, table_name)
                if table_exist:
                    with closing(conn.cursor()) as cursor:
                        if filters:
                            conditions = ' AND '.join([f"{column} = %s" for column in filters.keys()])
                            query = f"SELECT * FROM {table_name} WHERE {conditions}"
                            values = tuple(filters.values())
                        elif value:
                            columns = self.get_columns(db_name, table_name)
                            conditions = " OR ".join([f"{column} LIKE %s" for column in columns])
                            query = f"SELECT * FROM {table_name} WHERE {conditions}"
                            values = tuple(f"%{value}%" for column in columns)
                        else:
                            print("Could not get columns from the table.")
                            return "Fail"

                        cursor.execute(f"USE {db_name}")
                        cursor.execute(query, values)
                        result = cursor.fetchall()
                        for r in result:
                            print(r)
                    return "Pass"
                else:
                    print(f"The table '{table_name}' does not exist.")
                    return None
            except pymysql.MySQLError as e:
                print(f"Error querying table: {e}")
                return "Fail"

    def add_column(self, db_name, table_name, columns):
        """
        Adds a new column to the specified table.

        Args:
            db_name (str): The name of the database.
            table_name (str): The name of the table to add a column to.
            columns (dict): A dictionary where keys are column names and values are column types.

        Returns:
            str: "Pass" if column addition is successful, "Fail" if unsuccessful.
        """
        print("\nAdding column:")
        with self.manage_connection() as conn:
            try:
                table_exist = self.check_table_exist(db_name, table_name)
                if table_exist:
                    with closing(conn.cursor()) as cursor:
                        cursor.execute(f"USE {db_name}")
                        for column, col_type in columns.items():
                            query = f"ALTER TABLE {table_name} ADD COLUMN {column} {col_type}"
                            cursor.execute(query)
                        print(f"Column(s) added to table '{table_name}'.")
                    return "Pass"
                else:
                    print(f"The table '{table_name}' does not exist.")
                    return "Fail"
            except pymysql.MySQLError as e:
                print(f"Error adding column(s) to table: {e}")
                return "Fail"