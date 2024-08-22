# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = int(input('digite uma nota de 0 a 10 \n'))
if 0 <= nota < 4:
      print('nota classificada como baixa')
elif 4 <= nota < 8:
      print('nota considerada media') 
elif 8 <= nota < 10:
      print('nota conssiderada alta')
else:
      print('nota inesistente')      
