# 7) Búsqueda lineal (Intermedio)
# – Implementa una búsqueda lineal (sin funciones) sobre datos = [7, 2, 9, 4, 2] para hallar la
# PRIMERA ocurrencia de 2.
# – Imprime 'Encontrado en índice: i' o 'No encontrado' si no aparecee.
datos = [7, 2, 9, 4, 2]
ocurrencia = 2 
found = False   
for i in range(len(datos)):
    if datos[i] == ocurrencia:
        print(f"Encontrado en índice: {i}")
        found = True
        break
if not found:
    print("No encontrado")