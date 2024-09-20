def subtracao(n):
    if n == 1:
        return 1
    else:
        return n + subtracao(n - 1)
    
n=5
resultado = subtracao(n)
print(resultado)