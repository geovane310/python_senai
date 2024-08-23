# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mês = str(input('escolha um mês de 1 a 12 \n'))

if mês == '12' or mês== '1' or mês== '2':
     print(f'o mês {mês} é verão')
elif mês == '3' or mês == '4' or mês== '5':
        print(f'o mês {mês} é outono')
elif mês == '6' or mês== '7' or mês== '8':
          print(f'o mês {mês} é inverno')
elif mês == '9' or mês== '10' or mês== '11':
      print(f'o mês {mês} é primavera')
else:
      print('mes invalido')    
