import random 
n1 = int(input('Digite um número de 1 a 10: ')) 
n = random.randint(1,10)
erro = 1
while n1 != n:
    erro+=1 
    if n1 > n:
        print('Muito auto')
    else:
        print('Muito baixo')
    n1 = int(input('Tente novamente:')) 

print('O número que o computador escolheu foi {}.'.format(n))
print('Parabéns!')
print('Total de tentativa {}.'.format(erro))  


#chat gpt:
'''import random

# Gerar o número aleatório entre 1 e 10
n = random.randint(1, 10)

# Solicitar ao usuário que digite um número entre 1 e 10
n1 = int(input('Digite um número de 1 a 10: '))

# Inicializar o contador de tentativas
erro = 1

# Loop enquanto o número do usuário for diferente do número gerado
while n1 != n:
    erro += 1
    if n1 > n:
        print('Muito alto')
    else:
        print('Muito baixo')
    
    # Solicitar ao usuário que tente novamente
    n1 = int(input('Tente novamente:'))

# Quando o usuário acertar
print(f'O número que o computador escolheu foi {n}.')
print('Parabéns!')
print(f'Total de tentativas: {erro}.')
'''
