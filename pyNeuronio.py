
class Neuronio:

        def __init__(self, funcao_indice, listaPeso, taxaAprendizado, bias):
            listaFuncoes = [ lambda x : 1 if x > 0 else 0,
                             lambda x : 1 if x >= 0 else -1,
                             lambda x : 1 if x > 0 else (-1 if x < 0 else 0)
                           ]

            # Variaveis de inicializacao
            self.funcaoAtivacao = listaFuncoes[funcao_indice]    # Funcao de ativacao
            self.listaPeso = listaPeso      # Lista com valores de pesos de entrada
            self.taxa_n = taxaAprendizado   # Valor da taxa de aprendizado
            self.bias = bias                # Valor da bias

        def executar(self, listaEntrada):
            # Uk, Combinação linear
            somatoria = 0
            for num in range(len(self.listaPeso)):
                somatoria += (self.listaPeso[num] * listaEntrada[num])

            # Yk, Valor de saida
            yk = self.funcaoAtivacao(somatoria - self.bias)            
            return yk

        def correcao(self, listaEntrada, valorDesejado, valor_saida):
            '''
            Metodo de correcao dos valores de Peso
            Retorna o erroInstantaneo
            '''
            # ek, erro
            erro = valorDesejado - valor_saida
            # Verifica se o erro e zero
            if erro == 0 :
                return 0
            else:
                for indice in range(len(self.listaPeso)):
                    wDelta = self.taxa_n * erro * listaEntrada[indice]
                    self.listaPeso[indice] += wDelta
                return (1/2)*(erro*erro)