#!/usr/bin/python3
'''
Conecta con la Base de Datos y ejecuta queries
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
    user = sys.argv[1]
    password = sys.argv[2]
    data = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=data)

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()

