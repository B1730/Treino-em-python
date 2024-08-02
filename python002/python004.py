'''
n = int(input('Digite um núemro para descobrir seu fatorial:'))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    c-=1
    f *=c
    
print('O factorial de  {} é {}'.format(n,f))'''

cont = int(input("Qual o fatorial desejado?"))
soma = 1

while (cont > 0):
    soma = soma * cont
    cont = cont - 1

print("O fatorial é", soma)

