import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import pandas as csv
import pandas as pd

from condominio import Quadra, check_quadra, get_inicio, get_fim, create_receita_minibatch, create_custo_minibatch


# INPUT FINANCEIRO

taxa_juros = 0.05
taxa_desconto = 0.05
taxa_inflacao = 0.10
custos_fixos = 1000000
custos_variaveis = 0.05
imposto = 0.25


#Criando o condominio



df_quadras = pd.read_csv("quadras.csv", sep=",", header=0)
df_vendas = pd.read_csv("prognostico_venda.csv", sep=",", header=0)

#Conta o numero de quadras
n_quadras = df_quadras.Quadra.nunique()

#Lista do codominio. Cada elemento da lista é uma quadra.
condominio = []


fluxo_de_caixa = np.zeros(360) # 30 anos de fluxo_de_caixa
receita = np.zeros(360) # 30 anos de fluxo_de_caixa
custo = np.zeros(360) # 30 anos de fluxo_de_caixa

# Parse the df_quadra and return Quadra, Area Total, Receita Total por quadra
df_condominio = df_quadras.groupby("Quadra").agg({"Area": "sum", "Numero_de_Lotes": "sum"}).reset_index()

for row in df_condominio.itertuples():
    inicio_pag = get_inicio_pag(row, df_vendas)
    fim_pag = get_fim_pag(row, df_vendas)
    receita_minibatch = create_receita_minibatch(row, df_vendas)

    receita[inicio:fim] = receita[inicio:fim] + receita_minibatch

#     receita_minibatch = create_receita_minibatch(row, df_vendas)
#     custo_minibatch = create_custo_minibatch(row,df_vendas)
#
#     receita[inicio:fim] = receita[inicio:fim] + receita_minibatch
#     custo[inicio:fim] = custo[inicio:fim] + custo_minibatch




# Corretagem e impostos

corretagem = np.zeros(360)
impostos = np.zeros(360)

fluxo_de_caixa  = receita*0.3 - custo*0.3 - corretagem - impostos*0.3
valor_presente_liquido = npf.npv(taxa_desconto, fluxo_de_caixa)
print(f"R$ {valor_presente_liquido} é o valor presente liquido do condominio. Por irmao isso da R$ {valor_presente_liquido/3}")

#
# for i in range(32):
#     condominio.append(Quadra())
#     condominio[i].add_lote(n_lote=1, area=250)
#





