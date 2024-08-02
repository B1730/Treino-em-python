total= mas = vinte = 0
cadastro = 'S'
while True:
    if cadastro == 'S':
        idade = int (input('Digite sua idade:'))
        sexo = str(input('Qual seu sexo?[F/M]')).strip() .upper()
        if idade > 18:
            total +=1
        if sexo  ==  'M':
            mas+=1
        if sexo =='F' and idade < 20:
            vinte +=1
    cadastro = str(input('Quer cadastrar mais alguém?[S/N]')).strip() .upper()
    print('-'*40)
    if cadastro == 'N':
        break
print('='*40)
print(f'O total de pessoas com mais de 18 anos é {total}.')
print(f'Temos {mas} homens.')
print(f'Temos {vinte} mulhreres com menos de 20 anos.')
print('='*40)
