# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

numero = int(input('informe o numero: '))

for i in range(10):
      print(f'{numero} x {i +1} =', numero * (i+1))