# Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = str(input('escolha uma cor vermelho, verde, azul \n'))

if cor == 'vermelho':
      print('voce escolheu a cor vermelho!')
elif cor == 'azul':
      print("voce escolheu a cor azul!") 
elif cor == 'verde':
      print('voce escolheu a cor verde!')
else:
      print('cor não reconhecida')                