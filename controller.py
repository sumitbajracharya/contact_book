import mysql.connector
from contact_person import Contact_person

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.password = password
        self.database = database
        self.user = user
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user= self.user,
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

    def list_persons(self):
        try:
            sql = "SELECT * FROM persons"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            for row in rows:
                person = Contact_person(row[0], row[1], row[2]) 
                person.display()
                
        except mysql.connector.Error as err:
            print("Error listing persons:", err)

    def search_person(self, id):
        try:
            sql = "SELECT * FROM persons WHERE id = %s"
            self.cursor.execute(sql, (id,))
            row = self.cursor.fetchone()
            if row:
                person = Contact_person(row[0], row[1], row[2])
                person.display()
            else:
                print("Person not found")
        except mysql.connector.Error as err:
            print("Error searching person:", err)

    def delete_person(self, id):
        try:    
            sql = "DELETE FROM persons WHERE id = %s"
            self.cursor.execute(sql, (id,))
            self.conn.commit()
            print("Person deleted successfully")
        except mysql.connector.Error as err:
            print("Error deleting person:", err)

    def update_person(self, id, name, phone):
        try:
            sql = "UPDATE persons SET name = %s, phone = %s WHERE id = %s"
            self.cursor.execute(sql, (name, phone, id))
            self.conn.commit()
            print("Person updated successfully")
        except mysql.connector.Error as err:
            print("Error updating person:", err)
    

    def search_person_by_name(self, name):
        try:
            sql = "SELECT * FROM persons WHERE name LIKE %s"
            search_tearm = f"%{name}%"
            self.cursor.execute(sql, (search_tearm,))
            rows = self.cursor.fetchall()
            for row in rows:
                person = Contact_person(row[0], row[1], row[2])
                person.display()

            if not rows:
                print("Person not found")
        except mysql.connector.Error as err:
            print("Error searching person by name:", err)