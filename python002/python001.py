sexo = str(input('Digite seu sexo:')).strip()[0] #'[0]': So pegar a primeira leytra, eu posso escrever MASCULINO que só vai pegar o M 
while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido! Digite novamente:'))
print('Seu sexo é {} [M/F].'.format(sexo))
print('Confirmado!')
#Não utilizei o upper pois tem MmFf.