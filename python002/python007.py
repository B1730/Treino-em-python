
termo = int(input('Digite o termo: '))  # de onde inicia
pa = int(input('Digite a PA: '))  # De quanto em quanto pula
t = termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} - '.format(t), end='')
        t += pa
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja calcular? '))
print('Total de {} termos'.format(total))
    
print('Fim')
'''termo = int(input('Digite o termo inicial: '))  # De onde inicia
pa = int(input('Digite a razão da PA: '))  # De quanto em quanto pula

t = termo  # Termo atual
c = 1  # Contador de termos calculados
total = 0  # Total de termos calculados
mais = 10  # Inicialmente, calcular 10 termos

while mais != 0:
    total += mais
    while c <= total:
        print('{} - '.format(t), end='')
        t += pa
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja calcular? '))

print('Fim')'''
