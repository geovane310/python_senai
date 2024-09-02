frutas = ['acerola', 'maçã', 'uva', 'umbu']


def listar_frutas():
    for i in frutas:
        print(i)


def adicionar_fruta(nome):
    frutas.append(nome)


fruta = input('qual fruta deseja cadrastrar: ')

adicionar_fruta(fruta)
listar_frutas()

# teste 2

numeros = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
]