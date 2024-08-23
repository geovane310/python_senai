#  Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

maior = None 
for i in range(5):
      numero = int(input(f'informe o numero {i + 1} :'))

      if maior is None or numero > maior:
            maior = numero

print(f'O maior numero é: {maior}')            