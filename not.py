#testar com 0, 1, 34 e 5

a = int(input("Digite o valor de A:"))

if a:
    print("0 - false")
else:
    print("1 - true")

print(a>0)
print(not(a>0))
print(a!=0)
print(not(a==0))
y = not a
print(y)
z = not not a
print(z)
