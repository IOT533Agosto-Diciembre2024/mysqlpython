import mysql.connector
from mysql.connector import Error

def insert_data(director_no, director_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="andrestorres",
            database="videos"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = """INSERT INTO directors (director_no, director_name) VALUES (%s,%s)"""
            values = (director_no, director_name)
            cursor.execute(query, values)
            connection.commit()
            print("Registro insertado!! ")
    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def show_directors():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="andrestorres",
            database="videos"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = """SELECT * FROM directors"""
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print("Número: " + str(row[0]) + " Nombre: " + row[1])
    except Error as e:
        print(e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def desplegar_menu():
    print("0) Salir \n1) Insertar director \n2) Ver directores")


desplegar_menu()
option = input("Ingresa la opción: ")

while option != "0":
    if option == "1":
        director_no = input("Ingresa el número de director: ")
        director_name = input("Ingresa el nombre del director: ")
        insert_data(director_no, director_name)
    if option == "2":
        show_directors()
    desplegar_menu()
    option = input("Ingresa la opción: ")
