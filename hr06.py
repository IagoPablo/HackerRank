def soma_dos_digitos(numero):
    # Caso base
    if numero < 10:
        return numero
    else:
        # Separar o último dígito e somar com o resto dos dígitos
        return numero % 10 + soma_dos_digitos(numero // 10)


print(soma_dos_digitos(123))   # Deve retornar 6 (1 + 2 + 3)
print(soma_dos_digitos(4567))  # Deve retornar 22 (4 + 5 + 6 + 7)