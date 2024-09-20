def eh_primo(numero):
    divisiveis = []
    
    for numeros in range(1, numero+1):
        divisiveis.append(numeros)
        print(numeros)
    if numero % numeros == 0:
        print("é primo")
        print("Múltiplo de",numeros)
        return True
    elif numero == 0:
        print("é primo")
        return False
    else:
        print('não é primo')

eh_primo(4)


def eh_primo(numero):
    if numero < 2:
        return False  # Números menores que 2 não são primos
    
    # Verifica se algum número entre 2 e (n-1) divide 'numero'
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Se for divisível por 'i', não é primo
            return False
    
    return True  # Se não encontrou divisores, é primo

# Testando a função
print(eh_primo(4))  # Deve retornar False
print(eh_primo(7))  # Deve retornar True
