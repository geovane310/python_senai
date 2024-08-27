#  Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero1 = int(input('digite o primeiro numero\n'))
numero2 = int(input('digite o segundo numero\n'))
numero3 = int(input('digite o terceiro numero\n'))

maior = numero1
if numero2 > maior:
      maior = numero2
if numero3 >maior:
      numero3= numero3
print('o maior numero é:', maior)      