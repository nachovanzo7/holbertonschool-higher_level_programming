#!/usr/bin/python3

import json
"""
Modulo para serializar con json
"""
import csv
"""
Modulo para leer datos
"""

def convert_csv_to_json(archivocsv):
    lista = []
    try:
        with open(archivocsv, "r") as archivo:
            contenido = csv.DictReader(archivo)

            for x in contenido:
                lista.append(x)
        
        with open("data.json", "w") as archivojson:
            json.dump(lista, archivojson)

        return True

    except FileNotFoundError:
        print(f"Error: El archivo {archivocsv} no se encontró.")
        return False
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False
