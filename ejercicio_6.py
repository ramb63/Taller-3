# 6) Borrado conceptual con desplazamiento (Intermedio)
# – Dado arr = [4, 6, 8, 10, 12], borra el elemento en índice 2 
# desplazando a la izquierda los siguientes.
# – Rellena el último espacio con None y muestra el arreglo resultante
arr = [4, 6, 8, 10, 12]
erase = 2  
for i in range(erase, len(arr) - 1):
    arr[i] = arr[i + 1]
arr[-1] = None
print(arr)