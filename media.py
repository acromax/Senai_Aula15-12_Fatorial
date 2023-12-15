def media(valores):
    soma = 0
    for i in range(0, len(valores)):
        soma += valores[i]
    return soma/len(valores)

# Teste da média
x = [4, 5, 6, 7, 8, 9]
print('A média de ', end='')
for valor in x:
    print(f'{valor}, ', end='')
print(' é {:.2f}'.format(media(x)))
