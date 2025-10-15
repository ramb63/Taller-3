# 8) Traza de Burbuja (Intermedio)
# – Para a = [5, 1, 4, 2], realiza el método Burbuja en orden ascendente.
# – Escribe la traza tras cada pasada (no es necesario listar cada comparación) y luego imprime el
# arreglo ordenado
a = [5, 1, 4, 2]
print(a)
for i in range(1, len(a)):
    actual = a[i]
    j = i - 1
    while j >= 0 and a[j] > actual:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = actual

print(a)
