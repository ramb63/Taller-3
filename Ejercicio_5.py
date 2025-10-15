# 5) Inserción conceptual con desplazamiento (Intermedio)
# – Dado arr = [10, 20, 30, 40, None], inserta 25 en la posición 2 
# desplazando elementos a la derecha.
# – Muestra el estado del arreglo en cada paso del desplazamiento y el resultado final.
arr = [10, 20, 30, 40, None]
for i in range(3, 1, -1):
    arr[i + 1] = arr[i]
    print(arr)
arr[2] = 25
print(arr)