import csv

with open("ventas.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)