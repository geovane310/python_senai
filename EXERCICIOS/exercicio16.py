# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = str(input('escolha um tipo de combustivel\n'))

if combustivel == 'gasolina':
      print('gasolina: 6,50')
elif combustivel == 'etanol':
      print('etanol: 4,9')
elif combustivel == 'diesel':
      print('diesel: 6,03') 
else:
      print('combustivel indisponivel')           