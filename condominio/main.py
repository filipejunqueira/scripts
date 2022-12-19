import seaborn as sns
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import pandas as csv
import pandas as pd
from condominio import Condominio, random_list
import locale
locale.setlocale( locale.LC_ALL, '' )
np.random.seed(0)

nature = Condominio()
nature.add_lotes("prognostico_venda.csv")
n_lotes = nature.total_lotes()
#Initial VGV

print(f" \n VGV = R${round(nature.vgv(),2)}, Area total = {round(nature.total_area(),2)}, Total de lotes = {n_lotes}, Preco Medio por metro quadrado = {round(nature.average_price(),2)}")
print(f"Comecando fluxo de caixa")

######### INPUT FINANCEIRO #####################
taxa_desconto = 0.04
taxa_inflacao = 0.10
imposto = 0.25
permuta = 0.32

######### INPUT VENDA ###########################
range_venda = 24
center_venda = -3
std_venda = 4.1

range_parcelamento_entrada = 4
center_parcelamento_entrada = 4
std_parcelamento_entrada = 1.2

lote_mais_barato = 650 #A implementar
lote_mais_caro = 850   #A implementar
media = 700            #A implementar

######## INPUT CUSTOS ##########################
fee_marketing = 0.03  #9_000_000
inicio_pagamento_marketing = 0
periodo_marketing = 36
fee_corretagem = 0.05
fee_alienacao_fiduciaria = 0.05
despesas_extraordinarias = 0

########## OUTROS  #######################
adiantamento = (990_000+90000*3)*(1+taxa_inflacao)**(1/6)
modo_pagamento_adiantamento = 3  #0 So receita, 1 Receita - custo de receita, 2 Receita - custo de receita - custo de marketing, 3 - Receita - Custo total
inicio_pagamento_adiantamento = 3
corretagem_bruno = 3352*(725)
taxa_do_eu_nao_sabia = 0.90

######### INIT FLUXOS ##########################
size_fluxo = 12*60
fluxo_receita = np.zeros(size_fluxo)
fluxo_custo = np.zeros(size_fluxo)
fluxo_custo_marketing = np.zeros(size_fluxo)
fluxo_custo_receita = np.zeros(size_fluxo)
fluxo_adiantamento = np.zeros(size_fluxo)
fluxo_custo_extraordinario = np.zeros(size_fluxo)

entrada = np.zeros(n_lotes)
periodo_financiamento_list = np.zeros(n_lotes)
juros_list = np.zeros(n_lotes)
inadimplencia = np.zeros(n_lotes)
preco_m2_list = np.zeros(n_lotes)

# Ainda nao implementado ###########################
# range_entrada = 0.1
# center_entrada = 0.1
# std_entrada = 0.05
# periodo_financiamento = 120
# Ainda nao implementado ###########################

parcelamento_entrada_list, x_parcelamento_entrada, prob_parcelamento_entrada = random_list(center=center_parcelamento_entrada, std=std_parcelamento_entrada, size=range_parcelamento_entrada)
data_venda_list, x_venda, prob_venda = random_list(center=center_venda, std=std_venda, size=range_venda)

for i,row in enumerate(parcelamento_entrada_list):
    parcelamento_entrada_list[i] += 1

for i,row in enumerate(x_parcelamento_entrada):
    x_parcelamento_entrada[i] += 1

for i,parcela in enumerate(parcelamento_entrada_list):
    if parcela == 1:
        entrada[i] = 0.10
        periodo_financiamento_list[i] = 24
        juros_list[i] = 0.0
        inadimplencia[i] = 0.05
        preco_m2_list[i] = 700

    elif parcela == 2:
        entrada[i] = 0.15
        periodo_financiamento_list[i] = 36
        juros_list[i] = 0.0
        inadimplencia[i] = 0.05
        preco_m2_list[i] = 700

    elif parcela == 3:
        entrada[i] = 0.2
        periodo_financiamento_list[i] = 36
        juros_list[i] = 0.00
        inadimplencia[i] = 0.05
        preco_m2_list[i] = 700

    elif parcela >= 4:
        entrada[i] = 0.10
        periodo_financiamento_list[i] = 120
        juros_list[i] = 0.1
        inadimplencia[i] = 0.05
        preco_m2_list[i] = 700

    else:
        raise ValueError(f"Parcela Error in {i}")

periodo_financiamento_list = periodo_financiamento_list.astype(int)

########### Distribuicao de datas de venda e parcelamento #######################
nature.df_condominio['data_venda'] = data_venda_list
nature.df_condominio['parcelamento_entrada'] = parcelamento_entrada_list
nature.df_condominio['entrada'] = entrada
nature.df_condominio['financiamento'] = periodo_financiamento_list
nature.df_condominio['juros'] = juros_list
nature.df_condominio['inadimplencia'] = inadimplencia
nature.df_condominio['preco_m2'] = preco_m2_list
preco_medio = nature.df_condominio['preco_m2'].mean()
print(f"Preco medio: {preco_medio}")
print(f"Numero de lotes vendidos em menos de 3 meses = {len(data_venda_list[data_venda_list<3])}")

plt.bar(x_venda, height= prob_venda, label="velocidade de venda")
plt.title("Velocidade de venda")
plt.legend()
plt.xticks(np.arange(0, range_venda))
#plt.text(s=f"N lotes <= 3 meses = {n_lotes_trimestre}", y=2/3*np.max(prob_venda), x=range_venda/2, color='red')
plt.savefig("Prob_de_venda.png")
plt.show()

plt.bar(x_parcelamento_entrada, height=prob_parcelamento_entrada, label="parcelamento entrada")
plt.title("Prob de parcelamento da entrada")
plt.legend()
plt.xticks(x_parcelamento_entrada)
plt.savefig("Prob_de_parcelamento_entrada.png")
plt.show()

########## Distribuicao de Lotes ########################################

lotes_lais = nature.df_condominio[nature.df_condominio.dono == "Lais"]
lotes_paulo = nature.df_condominio[nature.df_condominio.dono == "Paulo"]
lotes_tais = nature.df_condominio[nature.df_condominio.dono == "Tais"]
lotes_bruno = nature.df_condominio[nature.df_condominio.dono == "Bruno"]
lotes_perplan = nature.df_condominio[nature.df_condominio.dono == "Perplan"]
lotes_quinan = nature.df_condominio[nature.df_condominio.dono == "Quinan"]

area_total = nature.df_condominio.area.sum()
area_perplan = lotes_perplan.area.sum()
area_quinan = lotes_quinan.area.sum()
area_lais = lotes_lais.area.sum()
area_paulo = lotes_paulo.area.sum()
area_tais  = lotes_tais.area.sum()
area_bruno = lotes_bruno.area.sum()

print(f"Area total = {area_total}, Area Perplan = {area_perplan}, Area Quinan = {area_quinan}, Area Lais = {area_lais}, Area Paulo = {area_paulo}, Area Tais = {area_tais}")
print(f"Distribuicao de Areas a venda:  Perplan = {area_perplan/area_total},  Quinan = {area_quinan/area_total}")

########## Determinacao da porcentagem de receita de cada irmao #########
area_a_dividir_quinan = area_total - area_perplan - area_bruno
area_por_irmao = (area_a_dividir_quinan)/3

area_divisivel=(area_a_dividir_quinan - area_lais - area_tais - area_paulo)

porcentagem_lais = (area_por_irmao - area_lais)/area_divisivel
porcentagem_paulo = (area_por_irmao - area_paulo)/area_divisivel
porcentagem_tais = (area_por_irmao - area_tais)/area_divisivel
print(f"Porcentagem de receita de cada irmao: Lais = {round(porcentagem_lais*100,2)}%, Paulo = {round(porcentagem_paulo*100,2)}%, Tais = {round(porcentagem_tais,2)*100}%")

########## FLUXO RECEITA ##########
for lote in lotes_quinan.itertuples():
    fluxo_lote = np.zeros(lote.parcelamento_entrada + lote.financiamento)
    corretagem = lote.preco_m2 * lote.area * fee_corretagem
    alienacao_fiduciaria = lote.preco_m2 * lote.area * fee_alienacao_fiduciaria

    #Entrada Parcelada
    for i in range(0,lote.parcelamento_entrada):
        fluxo_lote[i] = lote.preco_m2*lote.area*lote.entrada/lote.parcelamento_entrada

   #Parcelas
    for i in range(lote.parcelamento_entrada, lote.financiamento + lote.parcelamento_entrada):
        idx = i - lote.parcelamento_entrada
        fluxo_lote[i] = lote.preco_m2*lote.area*(1-lote.entrada)*((1+lote.juros)**(idx/12))/lote.financiamento
    start = lote.data_venda
    end = lote.financiamento + start + lote.parcelamento_entrada
    fluxo_receita[start:end] += fluxo_lote
    fluxo_custo_receita[start] += corretagem + alienacao_fiduciaria


############### Custos de Marketing #########################
valor_marketing = nature.vgv()* fee_marketing*permuta

for i in range(inicio_pagamento_marketing, inicio_pagamento_marketing + periodo_marketing):
    fluxo_custo_marketing[i] = valor_marketing/periodo_marketing


############### Custos extraordinarios ################################
for i in range(10,20):
    fluxo_custo_extraordinario[i] += nature.vgv()*despesas_extraordinarias/10

############### Adiantamento ################################
temp_adiantamento = adiantamento

if modo_pagamento_adiantamento == 0:
    for i,mes in enumerate(fluxo_receita[inicio_pagamento_adiantamento:]):
        idx = i + inicio_pagamento_adiantamento
        if temp_adiantamento > 0:
            if mes >= 0 and temp_adiantamento >= fluxo_receita[idx]/2:
                temp_adiantamento = temp_adiantamento - fluxo_receita[idx]/2
                fluxo_adiantamento[idx] = fluxo_receita[idx]/2
            elif mes >=0 and temp_adiantamento < fluxo_receita[idx]/2:
                fluxo_adiantamento[idx] = temp_adiantamento
                temp_adiantamento = 0
            elif mes < 0:
                pass
        if temp_adiantamento == 0:
            break

    #fluxo_custo += fluxo_adiantamento
    ############### Custos Corretagem + Alienacao fiduciaria ###########################
    # Corretagem e calculado em cima da receita e portanto so contabiliza a quota da familia
    #fluxo_custo += fluxo_custo_receita

if modo_pagamento_adiantamento == 1:
    diferenca = fluxo_receita[inicio_pagamento_adiantamento:] - fluxo_custo_receita[inicio_pagamento_adiantamento:]
    for i, mes in enumerate(diferenca):
        idx = i + inicio_pagamento_adiantamento
        if temp_adiantamento > 0:
            if mes >= 0 and temp_adiantamento >= diferenca[idx]/ 2:
                temp_adiantamento = temp_adiantamento - diferenca[idx] / 2
                fluxo_adiantamento[idx] = diferenca[idx] / 2
            elif mes >= 0 and temp_adiantamento < diferenca[idx] / 2:
                fluxo_adiantamento[idx] = temp_adiantamento
                temp_adiantamento = 0
            elif mes < 0:
                pass
        if temp_adiantamento == 0:
            break


if modo_pagamento_adiantamento == 2:
    diferenca = fluxo_receita[inicio_pagamento_adiantamento:] - fluxo_custo_receita[inicio_pagamento_adiantamento:] - fluxo_custo_marketing[inicio_pagamento_adiantamento:]
    for i, mes in enumerate(diferenca):
        idx = i + inicio_pagamento_adiantamento
        if temp_adiantamento > 0:
            if mes >= 0 and temp_adiantamento >= diferenca[idx]/ 2:
                temp_adiantamento = temp_adiantamento - diferenca[idx] / 2
                fluxo_adiantamento[idx] = diferenca[idx] / 2
            elif mes >= 0 and temp_adiantamento < diferenca[idx] / 2:
                fluxo_adiantamento[idx] = temp_adiantamento
                temp_adiantamento = 0
            elif mes < 0:
                pass
        if temp_adiantamento == 0:
            break

if modo_pagamento_adiantamento == 3:
        diferenca = fluxo_receita[inicio_pagamento_adiantamento:] - fluxo_custo_receita[
                                                                    inicio_pagamento_adiantamento:] - fluxo_custo_marketing[
                                                                                                     inicio_pagamento_adiantamento:] - fluxo_custo_extraordinario[inicio_pagamento_adiantamento:]
        for i, mes in enumerate(diferenca):
            idx = i + inicio_pagamento_adiantamento
            if temp_adiantamento > 0:
                if mes >= 0 and temp_adiantamento >= diferenca[idx] / 2:
                    temp_adiantamento = temp_adiantamento - diferenca[idx] / 2
                    fluxo_adiantamento[idx] = diferenca[idx] / 2
                elif mes >= 0 and temp_adiantamento < diferenca[idx] / 2:
                    fluxo_adiantamento[idx] = temp_adiantamento
                    temp_adiantamento = 0
                elif mes < 0:
                    pass
            if temp_adiantamento == 0:
                break
    ############### Custos Corretagem + Alienacao fiduciaria ###########################
    # Corretagem e calculado em cima da receita e portanto so contabiliza a quota da familia

############### Fluxo  final #######################################
fluxo_custo += fluxo_custo_receita
fluxo_custo += fluxo_adiantamento
fluxo_custo += fluxo_custo_marketing
fluxo_custo += fluxo_custo_extraordinario

fluxo = fluxo_receita - fluxo_custo
fluxo = fluxo*(1-imposto)*taxa_do_eu_nao_sabia
vpl = npf.npv(((1+taxa_desconto)**(1/12) -1), fluxo)

print(f"VPL = {locale.currency(round(vpl,2), grouping=True)}")
print(f"VPL por irmao = {locale.currency(round(vpl/3,2), grouping=True)}")

print(f"VPL Tais = {locale.currency(round(vpl*porcentagem_tais,10), grouping=True)}")
print(f"VPL Lais = {locale.currency(round(vpl*porcentagem_lais,10), grouping=True)}")
print(f"VPL Paulo = {locale.currency(round(vpl*porcentagem_paulo,10), grouping=True)}")

teste = porcentagem_lais + porcentagem_paulo + porcentagem_tais
print(f"SOMA Participacao= {teste}, deveria ser 1")

erro_bruno =  area_bruno*lotes_bruno.preco_m2.mean() - corretagem_bruno
erro_perplan = (area_perplan - 0.68*area_total)*lotes_perplan.preco_m2.mean()

print(f"Erro Bruno = {locale.currency(round(erro_bruno,2), grouping=True)}")
print(f"Erro Perplan = {locale.currency(round(erro_perplan,2), grouping=True)}")

figure, ax = plt.subplots(figsize=(24,24))
#plt.bar(x = np.arange(0,len(fluxo_receita)), height=fluxo_receita/3, label="Receita")
plt.plot(fluxo_receita/3, label="Receita" , color="blue", alpha =0.8)
ax.plot(fluxo/3, label="Fluxo", color = "green", linewidth=4, alpha = 0.8)
ax.plot(fluxo_adiantamento/3,label="Adiantamento", color = "cyan",alpha=0.8)
ax.plot(fluxo_custo_marketing/3, label="Marketing", color = "magenta" ,alpha=0.8)
ax.plot(fluxo_custo_receita/3, label="Corretagem + Alienacao", color = "red",alpha=0.8)
ax.plot(fluxo_custo_extraordinario/3, label="Custo Extraordinario", color = "pink",alpha=0.8)
#ax.plot(fluxo_custo/3, label="Custo Total", color = "black",alpha=0.8)

months_to_plot = 40
plt.xticks(np.arange(0, size_fluxo, 1))
plt.yticks(np.arange(round(1.05*np.min(fluxo[:months_to_plot]/3),-3), 1.02*np.max(fluxo_receita[:months_to_plot]/3), step=10_000))
plt.xlim([0,months_to_plot])
plt.legend(fontsize = 20)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
ax.tick_params(axis='both', which='major', labelsize=18)
plt.grid()
plt.savefig("fluxo.png")
plt.show()
####################################Plano de Investimento###################################

