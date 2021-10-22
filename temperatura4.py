# programa converte temperatura grau Celsius em Kelvin

print('OLÁ USUÁRIO(A) ! VAMOS TRABALHAR AS TEMPERATURAS CELSIUS E KELVIN !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

TC: float = float(input('DIGITE O VALOR DA TEMPERATURA EM GRAUS CELSIUS : '))

KLV: float = TC + 273.15

print('TEMPERATURA EM GRAUS CELSIUS : {:.2f}'.format(TC))
print('TEMPERATURA EM GRAUS KELVIN    : {:.2f}'.format(KLV))