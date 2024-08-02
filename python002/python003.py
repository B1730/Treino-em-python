n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
while True:
    print('=*='*12)
    print('''[1]somar\n[2]multiplicar\n[3]maior\n[4]outros números\n[5]sair do programa\n>>>>''')
    n3 = int(input('Qual é a sua opção? '))
    print('=*='*12)
    if n3 == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2,(n1+n2)))
    elif n3 == 2:
        n4 = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1,n2,n4))
    elif n3 == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        elif n2 > n1:
            print('O maior valor é {}'.format(n2))
        else:
            print('Os números são iguais.')
    elif n3 == 4:
        n1 = int(input('Primeiro vlor:'))
        n2 = int(input('Segundo valor:'))
    elif n3 == 5:
        print('Finalizando...')
        break #pra fechar.
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa.')
        
