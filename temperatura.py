# programa converte temperatura grau Celsius em Fahrenheit

print('OLÁ USUÁRIO(A) ! VAMOS TRABALHAR AS TEMPERATURAS CELSIUS E FAHRENHEIT !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

TC: float = float(input('DIGITE O VALOR DA TEMPERATURA EM GRAUS CELSIUS : '))

FH: float = TC * (9.0/5.0) + 32.0

print('TEMPERATURA EM GRAUS CELSIUS    : {:.2f}'.format(TC))
print('TEMPERATURA EM GRAUS FAHRENHEIT : {:.2f}'.format(FH))