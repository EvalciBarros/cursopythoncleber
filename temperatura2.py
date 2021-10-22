# programa converte temperatura grau Fahrenheit em Celsius

print('OLÁ USUÁRIO(A) ! VAMOS TRABALHAR AS TEMPERATURAS FAHRENHEIT E CELSIUS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

FH: float = float(input('DIGITE O VALOR DA TEMPERATURA EM GRAUS FAHRENHEIT : '))

TC: float = 5.0 * (FH - 32.0) / 9.0

print('TEMPERATURA EM GRAUS FAHRENHEIT : {:.2f}'.format(FH))
print('TEMPERATURA EM GRAUS CELSIUS    : {:.2f}'.format(TC))