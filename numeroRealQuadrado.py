# programa lê um número real e imprime seu quadrado

NUM: float = float(input('DIGITE UM NÚMERO REAL : '))
print ('VOCÊ DIGITOU O NÚMERO REAL : %f '%NUM)
print ('NÚMERO COM CASAS DECIMAIS REDUZIDAS É : {:.2f}'.format(NUM))

Quad: float = NUM**2

print('QUADRADO DO NÚMERO REAL DIGITADO NORMAL LIDO É : %f ' %Quad)
print('QUADRADO DO NÚMERO COM CASAS DECIMAIS REDUZIDAS É : {:.2f}'.format(Quad))

