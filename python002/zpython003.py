'''import random
comp=random.randint(1,10)
while True:
    n1= int(input('Digite um valor:'))
    pm = str(input('Par ou Impar:[P/I]')).upper()
    n2 = n1 + comp
    if n2 % 2 ==0 and pm == 'P':
        print('Voce venceu.')
        print('Vaos jagar novamente.')
        print(f'O comoputador escolheu {comp}. A soma é {n2}, portanto Par.')
    elif n2 % 2 != 0 and pm == 'I':
        print('Voce venceu!!')
        print('Vaos jagar novamente.')
        print(f'O comoputador escolheu {comp}. A soma é {n2}, portanto Impar.')
    else:
        break
print(f'Gamer OVER\n o computador escolheu {comp} a soma é {n2}')
print(f'Voce venceu {} vezes')'''
import random

vitorias = 0

while True:
    print('=*='*20)
    comp = random.randint(1, 10)
    n1 = int(input('Digite um valor: '))
    pm = str(input('Par ou Ímpar: [P/I] ')).upper()
    n2 = n1 + comp
    print('=*='*20)
    if n2 % 2 == 0 and pm == 'P':
        print('-'*20)
        print('Você venceu.')
        print('Vamos jogar novamente.')
        print(f'O computador escolheu {comp}. A soma é {n2}, portanto Par.')
        print('-'*20)
        vitorias += 1
    elif n2 % 2 != 0 and pm == 'I':
        print('-'*20)
        print('Você venceu!!')
        print('Vamos jogar novamente.')
        print(f'O computador escolheu {comp}. A soma é {n2}, portanto Ímpar.')
        vitorias += 1
        print('-'*20)
    else:
        print('#-#'*20)
        print(f'Game OVER\nO computador escolheu {comp} e a soma é {n2}.')
        print('#-#'*20)
        break

print(f'Você venceu {vitorias} vezes.')


