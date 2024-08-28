#  Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input('Imforme sua idade'))
if idade == 16 or idade >= 16:
      print('Já pode votar')
else:
      print('não pode votar')    