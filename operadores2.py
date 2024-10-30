dados = 0b10101     # 3° dado menos significativo é 0
mascara = 0b01000
print(dados & mascara)

dados = 0b11101     # 3° dado menos significativo é 1
mascara = 0b01000
print(dados & mascara)

dados = 0b111101
mascara = 0b110111
print(dados & mascara)

dados = 0b1000
mascara = 0b0111
print(dados | mascara)
