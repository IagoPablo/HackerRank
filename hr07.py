def maximo_lista(lista_de_numeros):
    if len(lista_de_numeros) == 1:
        print(len(lista_de_numeros))
        return lista_de_numeros[0]
    else:
        return lista_de_numeros >= maximo_lista(lista_de_numeros[0+1])
        
    
print(maximo_lista([5,3]))


def maximo_lista(lista_de_numeros):
    if len(lista_de_numeros) == 1:
        return lista_de_numeros[0]
    else:
        
        max_do_resto = maximo_lista(lista_de_numeros[1:])
        
        # Compara o primeiro elemento com o máximo do resto da lista
        if lista_de_numeros[0] > max_do_resto:
            return lista_de_numeros[0]
        else:
            return max_do_resto

# Teste a função
print(maximo_lista([5, 3, 9, 1, 7]))  # Deve retornar 9
print(maximo_lista([7, 7, 7]))  # Deve retornar 7