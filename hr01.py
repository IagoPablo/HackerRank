
# lista = [1,2,3,4,8,6,8,9]
# lista_pares = []

# def soma_pares(lista):
#     for x in lista:
#         if x % 2 == 0:
#             lista_pares.append(x)
            
#         soma = sum(lista_pares)
#     print(f'os numeros pares das listas são: {lista_pares}')
#     print(f'a soma de todos os numeros pares das listas são: {soma}')

# soma_pares(lista)


def soma_pares(lista):
    soma = 0
    lista_pares = []
    
    for x in lista:
        if x % 2 == 0:
            lista_pares.append(x)
            soma += x
            
    print(f'Os números pares da lista são: {lista_pares}')
    print(f'A soma de todos os números pares da lista é: {soma}')
    return soma

lista = [1, 2, 3, 4, 5, 6]
soma_pares(lista)
