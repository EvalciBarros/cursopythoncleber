# programa converte velocidade em km/h para m/s

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR AS VELOCIDADES KM/H E M/S !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

KMH: float = float(input('DIGITE O VALOR DA VELOCIDADE EM KM/H : '))

MS: float = KMH / 3.6

print('VELOCIDADE EM KM/H : {:.2f}'.format(KMH))
print('VELOCIDADE EM M/S  : {:.2f}'.format(MS))