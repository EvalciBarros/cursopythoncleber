# programa lê um número eal e imprime a 5a parte deste número

NUM1: float = float(input('DIGITE UM NÚMERO REAL : '))
print('VOCÊ DIGITOU O NÚMERO REAL : %f '%NUM1)
print('NÚMERO REDUZIDO À DUAS CASAS DECIMAIS É : {:.2f}'.format(NUM1))

Quinta: float = NUM1 / 5

print('QUINTA PARTE DO NÚMERO REAL DIGITADO É : %f ' %Quinta)
print('QUINTA PARTE DO NÚMERO COM DUAS CASAS DECIMAIS É : {:.2f}'.format(Quinta))