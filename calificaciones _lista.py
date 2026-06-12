import csv

with open("calificaciones.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
