#Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = int(input('digite o primeiro numero \n'))
numero2 = int(input('digite o segundo numero \n'))

if numero1 % 2 == 0 and numero2 % 2 == 0:
      print('ambos os numeros são pares')
else:
      print('um numero e par ou ambos são inpar')      