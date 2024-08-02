termo = int(input('Digite o termo: '))  # de onde inicia
pa = int(input('Digite a PA: '))  # de quanto em quanto pula
t = termo
c = 1
while c <=10:
    print('{} - '.format(t), end= '')
    t +=pa
    c+=1
print('Fim')