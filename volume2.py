# programa converte volume em litros para metros cúbicos

print('OLÁ USUÁRIO(A) ! AGORA VAMOS TRABALHAR VOLUMES EM LITROS PARA METROS CÚBICOS !!')
print('SIGA AS INSTRUÇÕES A SEGUIR')

LITROS: float = float(input('DIGITE O VALOR DO VOLUME EM LITROS : '))

MC: float = LITROS / 1000

print('VOLUMES EM LITROS         : {:.2f} L '.format(LITROS))
print('VOLUMES EM METROS CÚBICOS : {:.2f} m3 '.format(MC))
