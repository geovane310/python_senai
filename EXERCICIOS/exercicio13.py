# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mês = str(input('escolha um mês de 1 a 12 \n'))

if mês == '12' or '1' or '2':
     print(f'o mês {mês} é verão')
elif mês == '3' or '4' or '5':
        print(f'o mês {mês} é outono')
elif mês == '6' or '7' or '8':
          print(f'o mês {mês} é inverno')
elif mês == '9' or '10' or '11':
      print(f'o mês {mês} é primavera')
else:
      print('mes invalido')    
