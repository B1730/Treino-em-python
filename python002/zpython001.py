soma = cons = 0
while True:
    n1 = int(input('Digite um número:'))
    if n1 == 999:
        break
    cons += 1
    soma += n1

print(f'Você escolheu um total de {cons}, a soma deles é {soma}')
