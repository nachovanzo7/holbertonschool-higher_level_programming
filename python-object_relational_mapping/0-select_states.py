#!/usr/bin/python3
'''
Conecta con base de datos y ejecuta SQL query
'''

import MySQLdb
'''
MySQLdb - Ejecuta SQL queries
'''
import sys
'''
Interprete de python
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
