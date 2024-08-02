
n2 = 'S'
n1 = n2 = n3 = n4 = n5 = 0
while n2 == 'S':
    n1 = int(input('Digite um valor:'))
    n2 = str(input('Deseja continuar?[S/N]')).upper()
    n3 +=1
    n4 +=n1
    n5 = n4/n3
    if n3 == 1:
        m = n = n1
    else:
        if n1 < n:
            n = n1
        
        if n1 > m:
            m = n1
print('O menor número é {}e o maior número é {}'.format(n, m))
print('Você digitou {} números'.format(n3))
print('A media é {:.2f}'.format(n5))
    