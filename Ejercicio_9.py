# Burbuja optimizada y métricas (Avanzado)
# – Ordena ascendentemente a = [3, 2, 4, 1, 5] con Burbuja optimizada 
# (detén el algoritmo si no hay intercambios en una pasada).
# – Cuenta e imprime: comparaciones totales, intercambios totales y el arreglo final.
a = [3, 2, 4, 1, 5]
n = len(a)

comparaciones = 0
intercambios = 0

for pasada in range(n - 1):
    hubo_cambio = False
    for i in range(n - 1 - pasada):
        comparaciones += 1
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            intercambios += 1
            hubo_cambio = True
    print(f"Después de la pasada {pasada + 1}: {a}")
    
    if not hubo_cambio:
        print(" No hubo intercambios")
        break
print(f"i = {i}, comparaciones = {comparaciones}, intercambios = {intercambios}, arreglo= {a}")