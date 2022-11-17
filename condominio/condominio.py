import numpy as np

class Quadra:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.lista_lote = []

    def add_lote(self, n_lote=1, area=250):
        self.lista_lote.append([n_lote,area])


def check_quadra(df_block):
    return df_block.Quadra

def get_inicio_pag(df_block, df_vendas):
    quadra = check_quadra(df_block)
    return int(df_vendas[df_vendas.Quadra == quadra].Mes_de_Inicio_de_Venda.iloc[0])

def get_fim_pag(df_block, df_vendas):
    quadra = check_quadra(df_block)
    fim = df_vendas[df_vendas.Quadra == quadra].Mes_de_Inicio_de_Venda.iloc[0] + df_vendas[df_vendas.Quadra == quadra].Periodo_de_Venda.iloc[0]
    return int(fim)


def create_receita_minibatch(df_block, df_vendas):
    quadra = check_quadra(df_block)
    size_minibatch = df_vendas[df_vendas.Quadra == quadra].Periodo_de_Venda.iloc[0] + df_vendas[df_vendas.Quadra == quadra].Periodo_de_Financiamento.iloc[0]
    receita_minibatch = np.zeros(size_minibatch)
    #Boom de vendas inicial:
    venda_inicial =  df_vendas[df_vendas.Quadra == quadra].Venda_Inicial.iloc[0]
    preco_m2 = df_vendas[df_vendas.Quadra == quadra].Preco_m2.iloc[0]
    area = df_block.Area
    receita_minibatch[0] = venda_inicial*preco_m2*area
    for i in range(1, size_minibatch):
        #Entrada
        receita_minibatch[i] = receita_minibatch[i] + (1-venda_inicial)*preco_m2*area/(size_minibatch-1)
        #
    flagcheck = round(preco_m2*area,4)
    flagcheck2 = round(np.sum(receita_minibatch),4)
    if flagcheck != flagcheck2:
        print(f"ERRO, {flagcheck} vs {flagcheck2}")
    else:
        print("OK")


    return receita_minibatch

def create_custo_minibatch(quadra, df_vendas):
    pass
