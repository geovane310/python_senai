# Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

numero = int(input('Digite um numero\n'))

if numero == 0:
      print('numero é igual a zero')
elif numero > 0:
      print('numero é positivo')
elif numero < 0:
      print('numero é negativo')