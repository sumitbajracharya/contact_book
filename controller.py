import mysql.connector

class DatabaseManager:
    def __init__(self, host, password, database):
        self.host = host
        self.password = password
        self.database = database

        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL database")
        except mysql.connector.Error as err:    
            print("Error connecting to MySQL database:", err)

    def add_person(self, name, phone):
        try:
            sql = "INSERT INTO persons (name, phone) VALUES (%s, %s)"
            self.cursor.execute(sql, (name, phone))
            self.conn.commit()
            
            print("Person added successfully")
        except mysql.connector.Error as err:
            print("Error adding person:", err)