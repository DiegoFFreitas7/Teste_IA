from random import randint
from random import choices
from copy import copy

class Individuo:
    """Classe que representa cada individuo de uma populacao.
    """
    def __init__(self, genes, desempenho, min_value=None, max_value=None, restricao=None):
        """
        'genes' = Numero de genes a ser criado para este individuo ou um lista de genes pronta
        'desempenho' = Funcao que recebe o proprio genes do Individuo e calcula o seu desempenho
            Ex: lambda genes : genes[0]*2 + genes[1]*5 + genes[3]             
        'min_value' = menor valor possivel para um gene a ser criado
        'max_value' = maior valor possivel para um gene a ser criado
        'restricao' = Funcao caso exista alguma restricao no gene, de forma a zera o seu desempenho se o retorno for False
            Ex: lambda genes : genes[0] >= 0 and genes[1] >= 0
        """
        self.genes = genes
        self.desempenho = desempenho
        self.restricao = restricao

        if type(genes) == int:
            self.genes = [randint(min_value, max_value) for num in range(genes)]


    def cal_Desempenho(self):
        """Metodo que calcula o desempenho da lista de 'genes'
        atual do individuo.
            Se existir alguma restricao e nao for atendida
        a metodo retorna 0 (zero).
        """
        if self.desempenho != None:
            if self.restricao != None:
                if not self.restricoes():
                    return 0
            return self.desempenho(self.genes)
        return None
    
    def restricoes(self):
        """Metodo que verifica se a sequencia de genes
        atendem a 'restricao'.
        """
        if self.restricao != None:
            return self.restricao(self.genes)
        return None


class Algoritimo_Genetico:
    """Classe que implementa todas as funcoes
    do algoritimo genetico.
    """
    def __init__(self, populacao, taxa_mutacao, num_genes=None, min_value=None, max_value=None, desempenho=None, restricao=None):
        '''
        'populacao' = Numero da populacao a ser criada ou uma lista de Individuo
        'num_genes' = Quantidade de genes por Individuo a ser criado
        'min_value' = menor valor possivel para um gene a ser criado
        'max_value' = maior valor possivel para um gene a ser criado
        'desempenho' = funcao que recebe o proprio genes do Individuo e calcula o seu desempenho
            Ex: lambda genes : genes[0]*2 + genes[1]*5 + genes[3]  
        
        'restricao' = funcao caso exista alguma restricao no gene, de forma a zera o seu desempenho se o retorno for False
            Ex: lambda genes : genes[0] >= 0 and genes[1] >= 0
        '''
        self.taxa_mutacao = taxa_mutacao

        # Se a 'populacao' for um inteiro a propria classe deve criar os individuos
        if type(populacao) == int:
            self.populacao = []
            self.melhor = None

            # Se nao for passada nenhuma restricao, todos os genes sao gerados aleatoriamente
            if restricao == None:
                for num in range(populacao):
                    self.populacao.append(Individuo(num_genes, desempenho, min_value, max_value, restricao))
            
            # Se for passada uma restricao cada cromosomo sera criado e testado
            else:
                for num in range(populacao):
                    while(True):
                        cromosomo = [randint(min_value, max_value) for num in range(num_genes)]
                        if restricao(cromosomo):
                            break
                    self.populacao.append(Individuo(cromosomo, desempenho, restricao=restricao))

        # Se a 'populacao' nao for um inteiro, entao a classe so deve guardar a populacao recebida
        else:
            self.populacao = populacao
        
        # Calcula o melhor Indivuduo da populacao atual
        dict_populacao = {indice : self.populacao[indice].cal_Desempenho() for indice in range(len(self.populacao))}
        self.melhor = self.populacao[max(dict_populacao, key=lambda x : dict_populacao[x])]



    def nova_pop(self):
        '''Metodo calcula o melhor individuo da populacao atual
        e retorna uma nova geracao de individuo (nova populacao).
        '''

        # Gera um dicionario com o indice do individuo em self.populacao e o seu desempelho
        # dict = {indice : desempenho}
        # Ex: {0 : 80,
        #      1 : 110,
        #      2 : 5.7}
        dict_populacao = {indice : self.populacao[indice].cal_Desempenho() for indice in range(len(self.populacao))}
        
        # Copia o melhor individuo desta geracao
        self.melhor = copy(self.populacao[max(dict_populacao, key=lambda x : dict_populacao[x])])
        self.populacao = self.selecao_01(dict_populacao)

        return self.populacao

    def selecao_01(self, dict_populacao):
        '''Calcula a probabilidade de cada individuo ter decendentes
        e retorna os decendentes (nova populacao) dos cruzamentos
        entre os escolhidos.        
            Apenas o melhor individuo da populacao atual faz parte 
        da nova geracao.
            A probabilidade de selecao e igual ao desempenho do individuo pelo 
        desempenho geral.
        '''

        # Soma do desempenho geral da populacao
        soma = 0.001
        for key in dict_populacao:
            soma += dict_populacao[key]
        
        # key = indice do individuo
        # porcentagem = probabilidade de selecao
        keys = []
        porcentagem = []
        for key in dict_populacao:
            keys.append(key)
            porcentagem.append((100*dict_populacao[key])/soma)
        
        # Gera uma nova populacao do mesmo tamanho da anterior
        nova_populacao = [self.melhor]
        nova_populacao.append(self.populacao[choices(keys, porcentagem)[0]])
        while len(nova_populacao) < len(self.populacao):
            pai_1 = choices(keys, porcentagem)[0]
            limite = 10
            while limite > 0:
                limite -= 1
                pai_2 = choices(keys, porcentagem)[0]
                if pai_1 != pai_2:
                    break
            nova_populacao.append(self.cruzar_01(self.populacao[pai_1], self.populacao[pai_2]))
        return nova_populacao

    '''
    def selecao_02(self, dict_populacao, f_objetivo='MAXZ'):

        if f_objetivo == 'MAXZ':
            lista_indices = sorted(dict_populacao.items(), key=lambda x: x[1], reverse=True)
        else:
            lista_indices = sorted(dict_populacao.items(), key=lambda x: x[1])

        lista_porcentagem = []

        lista_porcentagem.append(0.25)
        lista_porcentagem.append(0.25)
        grupo = 2
        list_restante = len(lista_indices) - 2
        porcent_restante = 0.50

        while list_restante > 0:
            if list_restante > grupo + (grupo + 1):
                porcent_restante = porcent_restante/2
                lista_porcentagem.append(porcent_restante/2)
                lista_porcentagem.append(porcent_restante/2)
                list_restante -= 2
            else:
                porcent_restante = porcent_restante / list_restante
                for item in range(list_restante):
                    lista_porcentagem.append(porcent_restante)
                list_restante = 0
        

        keys = lista_indices
        porcentagem = lista_porcentagem

        # Gera uma nova populacao do mesmo tamanho da anterior
        nova_populacao = [self.melhor]
        nova_populacao.append(self.populacao[choices(keys, porcentagem)[0][0]])
        while len(nova_populacao) < len(self.populacao):
            pai_1 = choices(keys, porcentagem)[0][0]
            limite = 10
            while limite > 0:
                limite -= 1
                pai_2 = choices(keys, porcentagem)[0][0]
                if pai_1 != pai_2:
                    break
            nova_populacao.append(self.cruzar_01(self.populacao[pai_1], self.populacao[pai_2]))
        return nova_populacao
    '''

    def cruzar_01(self, pai_1, pai_2):
        '''Cruzamento 01
        '''
        # Cria um individuo filho como copia do pai_1
        filho = Individuo(copy(pai_1.genes), copy(pai_1.desempenho), restricao=copy(pai_1.restricao))
        
        # Se o cromossomo dos pais selecionados forem iguai
        # forca uma mutacao
        if pai_1.genes == pai_2.genes:
            filho = self.mutacao_01(filho)
            return filho

        # Sorteia a quantidade de genes que seram trocados
        qtde_genes = randint(1, len(pai_1.genes) -1)

        # Sorteia as posicoes dos genes que seram trocados
        posicoes_genes = []
        for vez in range(qtde_genes):
            posicao = randint(0, len(pai_1.genes) -1)
            if posicao not in posicoes_genes:
                posicoes_genes.append(posicao)

        # Troca os genes entre os pais (filho e copia de pai_1)
        for posicao in posicoes_genes:
            filho.genes[posicao] = pai_2.genes[posicao]
        
        # Sortei se ocorre mutacao
        if randint(1, 100) < self.taxa_mutacao:
            filho = self.mutacao_01(filho)
                
        return filho

    def mutacao_01(self, individuo):
        '''Mutacao 01
        '''
        
        # Sorteia a quantidade de genes que sofreram mutacao
        qtde_genes = randint(1, len(individuo.genes))

        # Sorteia as posicoes dos genes que sofreram mutacao
        posicoes_genes = []
        for vez in range(qtde_genes):
            posicao = randint(0, len(individuo.genes) -1)
            if posicao not in posicoes_genes:
                posicoes_genes.append(posicao)

        # Calcula a diferenca entre o maior e menor valor
        diferenca = max(individuo.genes) - min(individuo.genes)

        maior = int(max(individuo.genes) + diferenca)
        menor = int(min(individuo.genes) - diferenca)

        # Muta os genes
        for posicao in posicoes_genes:
            individuo.genes[posicao] = randint(menor, maior)
        
        return individuo
