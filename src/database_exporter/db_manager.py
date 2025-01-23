import mysql.connector
from mysql.connector import Error

# Az adatbázis menedzser osztály felelős az adatbázis kapcsolat kezeléséért.
class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return True
        except Error as e:
            print(f"Database connection error: {str(e)}")
            return False

    def get_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES")
        table_names = [table[0] for table in cursor]
        cursor.close()
        return table_names