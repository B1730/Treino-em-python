n1 = n = c = 0 #=> mais profissional
#n1 = 0
#n =0
#c = 0
while n1 !=999:
   n1 = int (input('Digite um número: [999] faz parar.'))
   
   if n1 != 999:
      n += n1
      c+=1
print('Você digitou {} números'.format(c))
print('A soma entre os números é {}'.format(n))
