"""
Modulo contiene funciones auxiliares
"""
import json
from os.path import join

def data_json(llave):
    """
    Lee parametros.json y retorna el valor del dato con la key correspondiente
    """
    ruta = join("parametros.json")
    with open(ruta, "r", encoding = "UTF-8") as archivo1:
        diccionario_data = json.load(archivo1)
    valor = diccionario_data[llave]
    return valor