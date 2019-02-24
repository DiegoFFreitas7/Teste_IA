from random import randint


def criarTxt(nome, linhas, min, max, qntdValores):
    '''
    Cria um arquivo txt com valores aleatorios
    linhas = quantidade de linhas do arquivo
    min = menor valor aleatorio
    max = maior valor aleatorio
    qntdValores = Quantidade de numeros em cada linha
    '''
    arquivo = open(nome, "w")

    for item in range(linhas):
        for valor in range(qntdValores):
            arquivo.write(str(randint(min, max)) + ', ')
        arquivo.write('\n')
    arquivo.close()

def lerTxt(nome):
    '''
    Le o txt criado pelo metodo acima e retorna
    uma lista com todas listas de numeros
    '''
    arquivo = open(nome, "r")

    lista_string = arquivo.read().split('\n')
    del lista_string[-1]

    listas_entradas = []
    lista_aux = []

    for item in lista_string:
        string_numeros = item.split(', ')
        del string_numeros[-1]
        for num in string_numeros:
            lista_aux.append(float(num))
        listas_entradas.append(lista_aux)
        lista_aux = []
    arquivo.close()
    return listas_entradas