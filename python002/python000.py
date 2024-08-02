'''for c in range (1,10):
    print(c)
print ('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c+=1 
print('Fim')'''

'''n1 = 'S'
while n1=='S':
    n= int(input('Digite um número:'))
    n1= str(input('Quer continuar? [S/N]')).upper()

print('Fim')'''

n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um número:'))
    if n != 0: #Para não contar o 0
        if n% 2 == 0:
            par +=1
        else:
            impar+=1
print('Você digitou {} pares e {} impas'.format(par, impar))