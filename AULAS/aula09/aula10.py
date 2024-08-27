# # #funcoes
# # numero1 = int(input('informe o numero:'))
# # numero2 = int(input('informe o numero:'))

# # print('a soma é:', numero1 + numero2)


# numeros = [1 , 5, 9, 6, 8, 7]

# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(sum(numeros))

# # media| recebe uma lista e tira a media dela 
# media = sum(numeros) / len(numeros)

# print(media)

# def media (numeros):
#      resultado = sum(numeros) / len(numeros)
#      return resultado

# print(media(numeros))    
# # soma| usada pra somar
# def soma (a, b):
#       soma = a + b
#       return soma
# print(soma(6, 7))   
# # funcao sem retorno
# def saudacao(nome):
#       print(f'Ola {nome}')

# # uso da função
# saudacao('Geovane')

# # funcão com parametro opicinal
# def ola(nome, mensagem='Olá'):
#       print(mensagem , nome)

# ola('Geovane', 'Oi')
# ola('Geovane')

# # função com multiplos retornos

# def dividir (numero1 , numero2):
#       resposta = numero1 // numero2
#       resto = numero1 % numero2
#       return resposta , resto


# divisao, resto_divisao = dividir(10, 2)

# print(divisao)
# print(resto_divisao)

# divisao = dividir(10, 2)

# print(divisao)

# numeros = (1 , 5, 9, 6, 8, 7)

# print(type(numeros))


# somar = lambda a, b: a + b 
# print(somar(10, 5))


# def exibir_imformacoes(*args):
#       print('argumentos posicionais:', args)


# exibir_imformacoes(1,4,'geovane', 'teste')


# def exibir_imformacoes2(**args):
#       print('argumentos nomeados:', args)

# exibir_imformacoes2(nome='geovane', idade=18, curso='python')
pessoas =[{
      'nome': 'Geovane',
      'idade': 18,
      'estado_civil': 'casado',
      'escolaridade': 'especialista'

},           
{


      'nome': 'Daniel',
      'idade': 19,
      'estado_civil': 'noivo',
      'escolaridade': 'superior'
}]         


print(pessoas[1])