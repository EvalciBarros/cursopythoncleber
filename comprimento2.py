# programa converte valores de comprimento em centímetros para polegadas

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR COMPRIMENTO MEDIDO EM CENTÍMETROS PARA POLEGADAS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

CM: float = float(input('DIGITE O VALOR DO COMPRIMENTO EM CENTÍMETROS : '))

POLEGADAS: float = CM / 2.54

print('MEDIDA EM CENTÍMETROS : {:.2f} CM '.format(CM))
print('MEDIDA EM POLEGADAS   : {:.2f} POLEGADAS '.format(POLEGADAS))
