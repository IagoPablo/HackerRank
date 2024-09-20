def verificar_palindromo(palavra):
        palavra_tras_pra_frente = palavra[::-1]
        for letras_palavra in palavra:
                lista1.append(letras_palavra)
        for letras_palavras_tras_pra_frente in palavra_tras_pra_frente:
                lista2.append(letras_palavras_tras_pra_frente)
        if lista1 == lista2:
                return True
        else:
               return False


lista1 = []
lista2 = []
verificar_palindromo('level')
print(lista1)
print(lista2)
print(lista1 == lista2)

def verificar_palindromo(palavra):
    # Inverte a palavra
    palavra_tras_pra_frente = palavra[::-1]
    
    # Compara a palavra original com a invertida
    if palavra == palavra_tras_pra_frente:
        return True
    else:
        return False

# Testando a função
print(verificar_palindromo('level'))  # Deve retornar True
print(verificar_palindromo('python'))  # Deve retornar False