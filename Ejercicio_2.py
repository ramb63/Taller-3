#) Recorrido y conteo (Básico)
#Con notas = [12, 8, 15, 19, 10, 14],
# recorre el arreglo y cuenta cuántas notas son ≥ 14.
# Imprime el mensaje: 'Cantidad de notas ≥ 14: X'

notas = [12, 8, 15, 19, 10, 14]
contar = 0
for nota in notas:
    if nota >= 14:
        contar += 1
print('cantidad de notas ≥ 14:', contar)