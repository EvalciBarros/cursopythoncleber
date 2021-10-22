# programa converte volume em metros cúbicos para litros

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR VOLUMES EM METROS CÚBICOS PARA LITROS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

MC: float = float(input('DIGITE O VALOR DO VOLUME EM METROS CÚBICOS : '))

LITROS: float = MC * 1000

print('VOLUMES EM METROS CÚBICOS : {:.2f} m3 '.format(MC))
print('VOLUMES EM LITROS         : {:.2f} L '.format(LITROS))
