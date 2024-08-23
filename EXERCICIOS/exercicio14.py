#  Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

numero1 = int(input('digite o primeiro numero\n'))
numero2 = int(input('digite o segundo numero\n'))
soma = numero1 + numero2

if soma > 100:
      print(' a soma dos numero é maior que 100')
elif soma == 100:
      print('a soma dos numero é igual a 100')
else:
      print('a soma do numro é menor que 100')            