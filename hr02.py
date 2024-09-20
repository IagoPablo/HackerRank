

def fatorial(n):
    lista_fatorial = []
    fatorar = 1
    for x in range(1, n +1):
        if n == 1:
            print('1! = 1')
        lista_fatorial.append(x)
    lista_fatorial.reverse()
    for x in lista_fatorial:
        fatorar *=x
    print(f'O fatorial de {n} é {fatorar}')
    return fatorar
    
fatorial(5)


# recursivo
def fatorial(n):
    if n == 0 or n == 1:  # Condição base: fatorial de 0 e 1 é 1
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva: multiplica n pelo fatorial de (n-1)

# Testando a função
n = 5
resultado = fatorial(n)
print(f'O fatorial de {n} é {resultado}')