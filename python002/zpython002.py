
c = 1
while True:
    n1 = int(input('Número que quer ver a tabuada:'))
    if n1 < 0:
        break
    for c in range(0, 11):
        print(f" {n1} x {c} = {n1*c}")
print('Fim')
