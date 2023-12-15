# Funções com uso de laço de repetição

# Tabuada
def tabuada(num):
    tabuada = []

    for i in range(1, 11):
        linha = f"{num} x {i} = {num * i}"
        tabuada.append(linha)

    return tabuada

# Teste Tabuada

tabuada = tabuada(2)
for linha in tabuada:
    print(linha)

