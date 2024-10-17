import mysql.connector
from mysql.connector import Error
from db_manager import DBManager


def desplegar_menu():
    print("0) Salir \n1) Insertar director \n2) Ver directores")


desplegar_menu()
option = input("Ingresa la opción: ")
db_manager = DBManager()
while option != "0":
    if option == "1":
        director_no = input("Ingresa el número de director: ")
        director_name = input("Ingresa el nombre del director: ")
        db_manager.insert_director(director_no, director_name)
    if option == "2":
        db_manager.show_directors()
    desplegar_menu()
    option = input("Ingresa la opción: ")
