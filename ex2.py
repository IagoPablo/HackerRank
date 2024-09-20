""""O programa deve gerar um número aleatório entre 1 e 100.
O usuário terá 5 tentativas para adivinhar o número.
A cada tentativa, o programa deve informar se o número secreto é maior ou menor do que o número inserido pelo usuário.
Se o usuário adivinhar o número corretamente, o programa deve parabenizá-lo e encerrar.
Se o usuário não adivinhar o número dentro do número de tentativas permitidas, o programa deve revelar o número secreto no final.



Use a função random.randint(1, 100) para gerar o número secreto.
Utilize um loop for ou while para gerenciar as tentativas do usuário.
Lembre-se de usar condicionais (if, elif, else) para verificar as respostas do usuário."""
import random
tentativas = 5;
numero_secreto = random.randint(1, 100);
print(numero_secreto)  
while tentativas >= 0:
    adivinhar = int(input('Tente adivinhar o numero secreto entre 1 a 100 '));
    if adivinhar != numero_secreto:
        tentativas -=1
        print(f'Numero incorreto, tentativas restants: {tentativas}')
        if adivinhar > numero_secreto:
            print('O numero adivinhado é maior que o numero secreto');
        elif adivinhar < numero_secreto:
            print('O numero adivinhado é menor que o numero secreto');
    if adivinhar == numero_secreto:
        print(f'Parábens você adivinhou o numero correto {numero_secreto}')
        break
    if tentativas == 0:
        print('Acabou suas tentativas')
        break

