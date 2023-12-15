# classe Fatorial

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

# Teste
print(f'\n {64}! = {fatorial(64)}')