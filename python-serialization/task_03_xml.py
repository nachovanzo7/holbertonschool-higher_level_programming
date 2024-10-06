#!/usr/bin/python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializa un diccionario a un archivo XML."""
    # Crear el elemento raíz
    root = ET.Element('data')

    # Iterar a través de los elementos del diccionario
    for key, value in dictionary.items():
        # Crear un elemento hijo para cada clave
        child = ET.Element(key)
        child.text = str(value)  # Convertir el valor a string
        root.append(child)

    # Crear un árbol de elementos y escribirlo en el archivo
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializa un archivo XML a un diccionario."""
    # Parsear el archivo XML
    tree = ET.parse(filename)
    root = tree.getroot()

    # Crear un diccionario para almacenar los datos
    result_dict = {}

    # Iterar sobre los elementos del archivo XML y agregarlos al diccionario
    for child in root:
        result_dict[child.tag] = child.text  # Recuperar los valores como texto

    return result_dict
