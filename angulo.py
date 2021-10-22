# programa converte ângulos em graus para radianos

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR ÂNGULOS EM GRAUS PARA RADIANOS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

GRAUS: float = float(input('DIGITE O VALOR DO ÂNGULO EM GRAUS : '))

RAD: float = GRAUS * 3.1418 / 180

print('ÂNGULO EM GRAUS    : {:.2f} GRAUS '.format(GRAUS))
print('ÂNGULO EM RADIANO  : {:.2f} RADIANOS '.format(RAD))