#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    # Crear el elemento raíz <data>
    root = ET.Element('data')
    
    # Iterar a través de los elementos del diccionario
    for key, value in dictionary.items():
        # Crear un elemento hijo para cada par clave-valor
        item = ET.SubElement(root, 'item', key=key)
        item.text = str(value)  # Convertir el valor a cadena
    
    # Crear el árbol XML y guardarlo en el archivo proporcionado
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

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
                pass
        
        dictionary[key] = value
    
    return dictionary
