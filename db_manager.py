import mysql
from mysql.connector import Error


class DBManager:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'videos'
        self.user = 'root'
        self.password = 'andrestorres'
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print(e)

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def insert_director(self,director_no,director_name):
        query = """INSERT INTO directors (director_no, director_name) VALUES (%s,%s)"""
        values = (director_no, director_name)
        self.cursor.execute(query, values)
        self.connection.commit()

    def show_directors(self):
        query = """SELECT * FROM directors"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            print("Número: " + str(row[0]) + " Nombre: " + row[1])