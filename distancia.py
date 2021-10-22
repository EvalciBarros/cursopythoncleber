# programa converte distância em milhas para kilômetros

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR AS DISTÂNCIAS EM MILHAS E QUILÔMETROS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

MILHAS: float = float(input('DIGITE O VALOR DA DISTÂNCIA EM MILHAS : '))

KMH: float = MILHAS * 1.61

print('DISTÂNCIA EM MILHAS : {:.2f} MILHAS '.format(MILHAS))
print('DISTÂNCIA EM KM  : {:.2f} KM '.format(KMH))
