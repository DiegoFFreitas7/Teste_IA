from random import randint
from algoritmo_Genetico import Individuo, Algoritimo_Genetico

'''
PROBLEMA

Existe 5 tipos de item a serem produzidos, e uma demanda
de no minimo 30 unidades de qualquer produto.
O custo de produção e quantidade maxima de produção 
de cada item esta descrito abaixo
    Item        Qtde_Max      Custo_producao(R$)
    item_A         10             40
    item_B         20            100
    item_C          5             10
    item_D         25             80
    item_E         30             70
Como se pode dividir a producao dos item de forma a ter o menor custo?
'''

'''
DEFINICAO DA SOLUCAO

    x1 = quantidade do item_A
    x2 = quantidade do item_B
    x3 = quantidade do item_C
    x4 = quantidade do item_D
    x5 = quantidade do item_E

Funcao objetivo / Desempenho
    Min_Z = item_A.valor*x1 + item_B.valor*x2 + item_C.valor*x3 + item_D.valor*x4 + item_E.valor*x5

Restricoes
    x1 + x2 + x3 + x4 + x5 >= 30

    x1 <= 10
    x2 <= 20
    x3 <= 5
    x4 <= 25
    x5 <= 30

    x1 >= 0
    x2 >= 0
    x3 >= 0
    x4 >= 0
    x5 >= 0
'''

# Definicao dos itens do problema
class Definicoes:
    def __init__(self, qtde, valor):
        self.qtde = qtde
        self.valor = valor

item_A = Definicoes(10, 40)
item_B = Definicoes(20, 100)
item_C = Definicoes(5, 10)
item_D = Definicoes(25, 80)
item_E = Definicoes(30, 70)
demanda = 30


num_populacao = 10
taxa_mutacao = 10
qtde_genes = 5 # Como sao 5 item, cada gene representa um item
min_gene = 0
max_gene = 30

# Calculo da funcao objetivo
desempenho = lambda genes : 1 / (item_A.valor*genes[0] + item_B.valor*genes[1] + item_C.valor*genes[2] + item_D.valor*genes[3] + item_E.valor*genes[4])

# Restricoes
res1 = lambda genes : (genes[0] + genes[1] + genes[2] + genes[3] + genes[4]) >= 30

res2 = lambda genes : genes[0] <= item_A.qtde
res3 = lambda genes : genes[1] <= item_B.qtde
res4 = lambda genes : genes[2] <= item_C.qtde
res5 = lambda genes : genes[3] <= item_D.qtde
res6 = lambda genes : genes[4] <= item_E.qtde

res7 = lambda genes : genes[0] >= 0
res8 = lambda genes : genes[1] >= 0
res9 = lambda genes : genes[2] >= 0
res10 = lambda genes : genes[3] >= 0
res11 = lambda genes : genes[4] >= 0

def res(genes):
    if res1(genes) and res2(genes) and res3(genes) and res4(genes) and res5(genes) and res6(genes) and res7(genes) and res8(genes) and res9(genes) and res10(genes) and res11(genes):
        return True
    else:
        return False

restricoes = lambda genes : res(genes)


teste = Algoritimo_Genetico(num_populacao, taxa_mutacao, qtde_genes, min_gene, max_gene, desempenho, restricoes)


print('-Populacao inicial---------')
for i in teste.populacao:
    print('Genes: ', i.genes, ' Desempenho: ', int(1/i.cal_Desempenho()), ' Custo: ', (item_A.valor*i.genes[0] + item_B.valor*i.genes[1] + item_C.valor*i.genes[2] + item_D.valor*i.genes[3] + item_E.valor*i.genes[4]))
print('Melhor:', teste.melhor.genes, int(1/teste.melhor.cal_Desempenho()))
print('-Populacao inicial---------')

print('')

for iteracao in range(1000):
    teste.nova_pop()
    #print('Melhor_' + str(iteracao) + ': ', 'Genes: ', teste.melhor.genes, ' Desempenho: ', teste.melhor.cal_Desempenho() )

print('-Populacao final-----------')
for i in teste.populacao:
    des = i.cal_Desempenho()
    if des > 0:
        des = int(1/des)
    else:
        des = 0
    print('Genes: ', i.genes, ' Desempenho: ', des, ' Custo: ', (item_A.valor*i.genes[0] + item_B.valor*i.genes[1] + item_C.valor*i.genes[2] + item_D.valor*i.genes[3] + item_E.valor*i.genes[4]))
print('Melhor:', teste.melhor.genes, int(1/teste.melhor.cal_Desempenho()))
print('-Populacao final-----------')


print('')

