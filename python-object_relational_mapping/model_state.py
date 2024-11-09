#!/usr/bin/python3
'''
Conecta con la Base de Datos y ejecuta queries
'''

from sqlalchemy import Column, Integer, String, create_engine
"""
Importa las clases y funciones necesarias 
para definir columnas en la base de datos y establecer la conexión.
"""
from sqlalchemy.ext.declarative import declarative_base
"""
Importa declarative_base, que es una fábrica para generar una clase base llamada Base
"""

Base = declarative_base()

class State(Base):
    """
    Clase state
    """
    
    #Nombre de la tabla que se va a crear en la Base de Datos
    __tablename__ = 'states'
    
    #Definir las columnas de dicha tabla
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# 
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
