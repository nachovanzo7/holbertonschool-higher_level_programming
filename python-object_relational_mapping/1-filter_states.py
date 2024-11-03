#!/usr/bin/python3
'''
Conecta con base de datos y ejecuta SQL query
'''

import MySQLdb
'''
Importa el módulo para interactuar con la base de datos MySQL
'''
import sys
'''
Importa el módulo para acceder a los argumentos de la línea de comandos
'''
if __name__ == "__main__":
    usuario = sys.argv[1]
    password = sys.argv[2]
    datos = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usuario,
        passwd=password,
        db=datos
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

