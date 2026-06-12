import csv
archivo_csv = "calificaciones.csv"
suma_promedios_grupo = 0
total_alumnos = 0
aprobados = 0
reprobados = 0
mejor_alumno = ""
peor_alumno = ""
mejor_promedio = -1
peor_promedio = 101
lista_alumnos = []
try:
    with open(archivo_csv, "r") as archivo:
        lector = csv.reader(archivo)
        next(lector) 
        
        for fila in lector:
            nombre = fila[1]
            p1, p2, p3 = int(fila[3]), int(fila[4]), int(fila[5])
            
            promedio_alumno = (p1 + p2 + p3) / 3
            
            suma_promedios_grupo += promedio_alumno
            total_alumnos += 1
            
            if promedio_alumno >= 70:
                aprobados += 1
            else:
                reprobados += 1
            
            if promedio_alumno > mejor_promedio:
                mejor_promedio = promedio_alumno
                mejor_alumno = nombre
                
            if promedio_alumno < peor_promedio:
                peor_promedio = promedio_alumno
                peor_alumno = nombre
            
            lista_alumnos.append((nombre, promedio_alumno))

    if total_alumnos > 0:
        promedio_general = suma_promedios_grupo / total_alumnos
        print("Resultados del análisis de calificaciones")
        print(f" {total_alumnos}  el promedio general del grupo quedó en {promedio_general:.2f}.")
        print(f" {aprobados} alumnos lograron aprobar la materia, mientras que {reprobados} fueron reprobados.")
        print(f" el promedio más alto lo obtuvo {mejor_alumno} con un total de {mejor_promedio:.2f}, que el más bajo fue el de {peor_alumno} con {peor_promedio:.2f}.\n")
        lista_alumnos.sort(key=lambda x: x[1], reverse=True)
        
        print("Lista ordenada de alumnos de mayor a menor promedio:")
        for puesto, (nombre, promedio) in enumerate(lista_alumnos, start=1):
            print(f"Posición {puesto}: {nombre} con un promedio de {promedio:.2f}")
            
    else:
        print("No se encontraron registros de alumnos para procesar en el archivo.")

except FileNotFoundError:
    print(f"No pude encontrar el archivo '{archivo_csv}'. Revisa que esté en la misma carpeta.")