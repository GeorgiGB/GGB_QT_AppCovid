import sqlite3
from sqlite3 import Error
import os

# Con esta funcion lo que haremos sera conectarnos a la base de datos que hemos creado previamente
def connectBD():
    try:
        conectar = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'Usuarios.db'))
        return conectar
    # Si no existiera se daria una excepcion
    except Error:
        print("Error")

# Con esta funcion lo que haremos es que se nos permita leer dentro de lo que hay en la base de datos
def readBD(user, passwd):
    cursorObj = connectBD().cursor()
    cursorObj.execute('Select * from Usuarios Where user =\'{}\' And passwd = {};'.format(user, passwd))
    try:
        resBD = cursorObj.fetchone()
        return resBD
    except:
        return "Error"
