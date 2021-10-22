# programa converte velocidade em m/s para km/h

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR AS VELOCIDADES M/S E KM/H !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

MS: float = float(input('DIGITE O VALOR DA VELOCIDADE EM M/S : '))

KMH: float = MS * 3.6

print('VELOCIDADE EM M/S : {:.2f}'.format(MS))
print('VELOCIDADE EM KM/H  : {:.2f}'.format(KMH))