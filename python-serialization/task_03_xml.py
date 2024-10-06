#!/usr/bin/python3

import xml.etree.ElementTree as ET

def deserialize_from_xml(filename):
    # Parsear el archivo XML
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Reconstruir el diccionario
    dictionary = {}
    for item in root:
        key = item.attrib['key']
        value = item.text
        
        # Tratar de convertir el valor a int o float si es posible
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass  # Mantener como cadena si no es un número
        
        dictionary[key] = value
    
    return dictionary
