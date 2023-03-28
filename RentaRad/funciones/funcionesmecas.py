import csv

def leer_bicicletas_csv(nombre_archivo):
    bicicletas = {}
    with open(nombre_archivo, newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            nombre = fila['Nombre']
            tipo = fila['Tipo']
            tamaño = fila['Tamaño']
            color = fila['Color']
            precio = float(fila['Precio por hora'])
            bicicletas[nombre] = {'Tipo': tipo, 'Tamaño': tamaño, 'Color': color, 'Precio por hora': precio}
    return bicicletas

import csv

import csv

def read_csv_to_dict(file_path):
    """
    Lee un archivo CSV y guarda los datos en un diccionario.
    Cada fila del archivo CSV se convierte en un registro de diccionario.
    """
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    return data

