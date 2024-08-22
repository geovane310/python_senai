#  Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = str(input('escolha um meio de transporte\n'))
if transporte == 'carro':
      print('carro:100km\h')
elif transporte == 'bicicleta':
      print('bicicleta: 25km\h')
elif transporte == 'a pé':
      print('a pé:3,6km\h')
else:
      print('fica em casa então')                  