# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida

operação = str(input('digite uma operação (+, -, *, /) \n'))
numero1 = float(input('digite o primerio numero \n'))
numero2 = float(input('digite o segundo numero \n'))
if operação == '+':
      resultado = numero1 + numero2
      print(f'o resultado de {numero1} + {numero2} é {resultado}')
elif operação == '-':
      resultado = numero1 - numero2
      print(f'o resultado de {numero1} - {numero2} é {resultado}')
elif operação == '*':
      resultado = numero1 * numero2
      print(f'o resultado de {numero1} * {numero2} é {resultado}')
elif operação == '/':
      resultado = numero1 / numero2
      print(f'o resultado de {numero1} / {numero2} é {resultado}')
else:
      print('nao existe essa operação')            