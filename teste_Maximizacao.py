from random import randint
from algoritmo_Genetico import Individuo, Algoritimo_Genetico

'''
PROBLEMA

Existe 3 tipos de item para se colocar em uma caixa de capacidade igual a 20Kg
A massa, valor e peso de cada item e descrito abaixo
    Item        Quantidade      Massa(Kg)   Valor(R$)
    item_A          3             3             40
    item_B          2             5            100
    item_C          5             2             50
Como se pode colocar os item na caixa de forma a obter o melhor valor?
'''

'''
DEFINICAO DA SOLUCAO

    x1 = quantidade do item_A
    x2 = quantidade do item_B
    x3 = quantidade do item_C

Funcao objetivo / Desempenho
    Max_Z = item_A.valor*x1 + item_B.valor*x2 + item_C.valor*x3

Restricoes
    item_A.massa*x1 + item_B.massa*x2 + item_C.massa*x3 <= 20

    item_A.qtde <= 3
    item_B.qtde <= 2
    item_C.qtde <= 5

    item_A.qtde >= 0
    item_B.qtde >= 0
    item_C.qtde >= 0
'''

# Definicao dos itens do problema
class Definicoes:
    def __init__(self, qtde, massa, valor):
        self.qtde = qtde
        self.massa = massa
        self.valor = valor

item_A = Definicoes(3, 3, 40)
item_B = Definicoes(2, 5, 100)
item_C = Definicoes(5, 2, 50)
limite_peso = 20


num_populacao = 10
taxa_mutacao = 10
qtde_genes = 3 # Como sao 3 item, cada gene representa um item
min_gene = 0
max_gene = 5

desempenho = lambda genes : item_A.valor*genes[0] + item_B.valor*genes[1] + item_C.valor*genes[2]
'''
# ou de forma mais visual

def des(genes):
    soma_dos_valores = item_A.valor*genes[0] + item_B.valor*genes[1] + item_C.valor*genes[2]
    return soma_dos_valores

desempenho = lambda genes : des(genes)
'''


restricoes = lambda genes : ((item_A.massa*genes[0] + item_B.massa*genes[1] + item_C.massa*genes[2]) <= limite_peso) and (genes[0] <= item_A.qtde) and (genes[1] <= item_B.qtde) and (genes[2] <= item_C.qtde) and (genes[0] >= 0) and (genes[1] >= 0) and (genes[2] >= 0)

'''
# ou de forma mais visual

res1 = lambda genes : item_A.massa*genes[0] + item_B.massa*genes[1] + item_C.massa*genes[2]) <= limite_peso
res2 = lambda genes : genes[0] <= item_A.qtde
res3 = lambda genes : genes[1] <= item_B.qtde
res4 = lambda genes : genes[2] <= item_C.qtde
res5 = lambda genes : genes[0] >= 0
res6 = lambda genes : genes[1] >= 0
res7 = lambda genes : genes[2] >= 0

def res(gense):
    if res1 and res2 and res3 and res4 and res5 and res6 and res7:
        return True
    else:
        return False

restricoes = lambda genes : res(gense)
'''

teste = Algoritimo_Genetico(num_populacao, taxa_mutacao, qtde_genes, min_gene, max_gene, desempenho, restricoes)


print('-Populacao inicial---------')
for i in teste.populacao:
    print('Genes: ', i.genes, ' Desempenho: ', i.cal_Desempenho(), ' Kilos: ', (item_A.massa*i.genes[0] + item_B.massa*i.genes[1] + item_C.massa*i.genes[2]))
print('Melhor:', teste.melhor.genes, teste.melhor.cal_Desempenho())
print('-Populacao inicial---------')

print('')

for iteracao in range(100):
    teste.nova_pop()
    #print('Melhor_' + str(iteracao) + ': ', 'Genes: ', teste.melhor.genes, ' Desempenho: ', teste.melhor.cal_Desempenho() )

print('-Populacao final-----------')
for i in teste.populacao:
    print('Genes: ', i.genes, ' Desempenho: ', i.cal_Desempenho(), ' Kilos: ', (item_A.massa*i.genes[0] + item_B.massa*i.genes[1] + item_C.massa*i.genes[2]))
print('Melhor:', teste.melhor.genes, teste.melhor.cal_Desempenho())
print('-Populacao final-----------')


print('')

