# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estado = str(input('qual seu estado civil\n'))
if estado == 'solteiro':
      print('voce precisa de uma mulher')
elif estado == 'casado':
      print('voce deve se separar')
elif estado == 'divorciado':
      print('vc prcisa pagar a pensão')
elif estado == 'viúvo':
      print('sua mulher morreu')
else:
      print('voce esta morto')                  


