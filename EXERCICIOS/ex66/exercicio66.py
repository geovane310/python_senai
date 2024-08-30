
from os import system
import operacoes as op
#from operacoes import menu , listar_nomes
#import operacoes

operacao = 'sim'

while operacao == 'sim':
      op.menu()
      opcao = int(input('imforme a ação desejada\n'))
      match opcao:
            case 1:
                  nome = input('que nome deseja cadastra: ')
                  op.cadastrar_nome(nome)
            case 2:
                 nome = input('que nome deseja atualizar?')
                 novo_nome = input('qual sera o novo nome?')
                 
                 op.atualiza_nome(nome, novo_nome)
            case 3:
                  nome = input('que nome deseja remover? ')
                  op.excluir_nome(nome)
            case 4:
              op.listar_nomes()
            case _:
                  print('opção invalida')

      operacao = input('Deseja realizar outra operação?').lower()
      system('clear')

      if operacao != 'sim':
            break
      