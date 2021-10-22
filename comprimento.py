# programa converte valores de comprimento em polegadas para centímetros

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR COMPRIMENTO MEDIDO EM POLEGADAS PARA CENTÍMETROS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

POLEGADAS: float = float(input('DIGITE O VALOR DO COMPRIMENTO EM POLEGADAS : '))

CM: float = POLEGADAS * 2.54

print('MEDIDA EM POLEGADAS   : {:.2f} POLEGADAS '.format(POLEGADAS))
print('MEDIDA EM CENTÍMETROS : {:.2f} CM '.format(CM))