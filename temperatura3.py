# programa converte temperatura grau Kelvin em Celsius

print('OLÁ USUÁRIO(A) ! VAMOS TRABALHAR AS TEMPERATURAS KELVIN E CELSIUS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

KLV: float = float(input('DIGITE O VALOR DA TEMPERATURA EM GRAUS KELVIN : '))

TC: float = KLV - 273.15

print('TEMPERATURA EM GRAUS KELVIN : {:.2f}'.format(KLV))
print('TEMPERATURA EM GRAUS CELSIUS    : {:.2f}'.format(TC))