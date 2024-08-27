# . Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

numeros1 = int(input('digite o primeiro numero\n'))
numeros2 = int(input('digite o segundo numero\n'))

if numeros1 % 5 == 0 and numeros2 % 5 == 0:
      print('ambos são multiplos de 5')
else:
      print('não são multiplos de 5')      