# classe Fatorial

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

# Teste
print(f'\n {64}! = {fatorial(64)}')

def  fatoria_recursivo(num):
    if num > 1
        fat = num * fatoria_recursivo(num -1)
        return fat
    else:
        return 1
