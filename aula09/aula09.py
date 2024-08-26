texto = 'geovane de França Santiago      '


texto2 = texto.capitalize()
# capitalaze| muda o primeiro caracter da string para maiusculo
print(texto.capitalize())
print(texto2)

# lower| padroniza a string em minusculo

nome = 'geovanE De FRAnça sANTIago'
nome2 = "geovane de frança santiago"
print(nome.lower())

if nome.lower() == nome2.lower():
      print('são iguais')
else:
      print('não são iguais')      

# upper| padroniza uma string em maiusculas

print(nome.upper())


# replace| muda um padrão de caractere de uma string

silvano_sales = 'coração coração cabeção'

# silvano_sales2 = silvano_sales.replace('ç','c')
# silvano_sales2 = silvano_sales.replace('ã','a')

print(silvano_sales.replace('çã', 'ca'))

# strip| é uma forma de remover caracteres em branco no final e no inicio de uma string

jack_stripador = '            removendo espaços de uma string          '

print(jack_stripador)
print(jack_stripador.strip())

# split| 

string_espalhada = 'Geovane de frança santiago'
print(string_espalhada)
print(string_espalhada.split())

# join| transforma os elementos de uma lista em uma string, concatena strings

nome_lista = ['geovane', 'frança', 'santiago']

print(' '.join(nome_lista))


# slice| manipula string por indice


cidade = 'Recando das emas, cidade do povo'

print(cidade[::-1])

palindromo = 'Arara'
 
if palindromo.lower() == palindromo[::-1].lower():
      print('é palindromo')
else:
      print('não é palindromo')      