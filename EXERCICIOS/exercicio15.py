# Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos

#primeira forma

idade = int(input('digite uma idade\n'))

if 13 <= idade <= 17:
      print('é adolecente')      
else:
      print('não é mais adolecente')            

#segunda forma 

# if idade >= 13 and idade <=17:
#       print('é adolecente')
# else:
#       print('nao é adolecente')            