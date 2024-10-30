num = int(input("Escreva um número: "))
etapa = 0

while num != 1:
    if num == 0:
        print("Número deve ser diferente de zero")
        break
    if num % 2 == 0:
        num = num / 2
        print(int(num))
    else:
        num = num * 3 + 1
        print(int(num))
    etapa += 1
print("Etapas:",etapa)
