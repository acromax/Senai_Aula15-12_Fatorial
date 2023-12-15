# algoritmo de ordenação em bolha

# Apresentação
print('\n\t\t -- Bubble Sort -- ')
#num1 = 37
#num2 = 8

numeros = [37, 8 , 1024, 14]

# Processamento
for i in range(1, len(numeros) -1):
    for j in range(i+1, len(numeros)):
        if numeros[i] > numeros[j]:
            swap = numeros[j]
            numeros[j] = numeros[i]
            numeros[i] = swap

# Saída
#print(f'{num1}, {num2})
for numero in numeros:
    print(f'{numero} ', end='')
