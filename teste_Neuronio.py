from random import randint
from algoritmo_Genetico import Individuo, Algoritimo_Genetico
from pyNeuronio import Neuronio
from manipulaArquivo import lerTxt, criarTxt
import matplotlib.pyplot as plt

# Valores iniciais
funcaoAtivacao = 1 # lambda x : 1 if x >= 0 else -1
tx = 0.5           # A "importancia/peso" que cada ciclo de aprendizado vai ter em cada valor de PESO do neuronio
bias = 1           # Não faço ideia. Deus quis.

listaEntrada = lerTxt('listaEntrada.txt')

saida = lerTxt('valoresDesejados.txt')[0] # Valores desejados para cada lista de entrada


num_populacao = 10
taxa_mutacao = 10
qtde_genes = len(listaEntrada[0]) # Como sao 4 itens, na lista cada gene representa um item
min_gene = -5
max_gene = 5


# Neuronio
n1 = Neuronio(funcaoAtivacao, [], tx, bias)


# Funcao que calcula o desempenho dos genes
def teste_desempenho(genes):

    # Neuronio recebe os genes
    n1.listaPeso = genes

    # Contador de acertos
    contador = 0

    # Executa o teste para cada valor na lista de entrada 
    for indice in range(len(listaEntrada)):
        retorno = n1.executar(listaEntrada[indice])

        # Adiciona 1 em contador se ele acertou a saida
        if retorno == saida[indice]:
            contador += 1
    
    return contador

desempenho = lambda genes : teste_desempenho(genes)

# Nao existe restricoes para os valores dos genes
restricoes = None


teste = Algoritimo_Genetico(num_populacao, taxa_mutacao, qtde_genes, min_gene, max_gene, desempenho, restricoes)


print('-Populacao inicial---------')
for i in teste.populacao:
    print('Genes: ', i.genes, ' Numero de acertos: ',i.cal_Desempenho())
print('Melhor:', teste.melhor.genes, teste.melhor.cal_Desempenho())
print('-Populacao inicial---------')
print('')

melhores = []
ite = 1000
for iteracao in range(ite):
    melhores.append(teste.melhor.cal_Desempenho())
    teste.nova_pop()

print('-Populacao final-----------')
for i in teste.populacao:
    print('Genes: ', i.genes, ' Numero de acertos: ',i.cal_Desempenho())
print('Melhor:', teste.melhor.genes, teste.melhor.cal_Desempenho())
print('-Populacao final-----------')
print('')

print('Maior acerto a cada iteração: ')
print(melhores)
iteracoes = [num for num in range(ite)]

plt.plot(iteracoes, melhores, color='lightblue', linewidth=3) #
plt.xlim(0, ite) # Valore limite de x
plt.title('Acertos dos melhores individuos em um período de ' + str(ite) + ' iterações') #adicionando o título
plt.xlabel('Quantidade de iterações')
plt.ylabel('Numero de Acertos')
plt.show()