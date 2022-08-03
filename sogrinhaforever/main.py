import finance
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
t = 10
c = 1100000
imposto = 0
c = c*(1-imposto)
j = 0.03
r_min = 0
inv = -10000

f = finance.Fluxo_de_caixa(tempo = t,capital=c, taxa = j)
fluxo_caixa_ref = f.flux(cupom = r_min)

f = finance.Fluxo_de_caixa(tempo = t,capital=c, taxa = j)
fluxo_caixa_invest = f.flux(cupom = inv)

f_intermediario = finance.Fluxo_de_caixa(tempo = t,capital=c, taxa = j)
new_flux_intermediario, renda_mensal_intermediaria = f_intermediario.renda(chute = 200 ,final=500000,tolerancia=0.05,lr = 0.1)


f_zero = finance.Fluxo_de_caixa(tempo = t,capital=c, taxa = j)
new_flux_zero, renda_mensal_zero = f_zero.renda(chute = 1, final=0, tolerancia=0.05, lr = 0.1)


fluxo_caixa_invest = np.round(fluxo_caixa_invest, decimals=2)
new_flux_zero = np.round(new_flux_zero, decimals=2)
fluxo_caixa_ref = np.round(fluxo_caixa_ref, decimals=2)
renda_mensal_zero = np.round(renda_mensal_zero, decimals=2)
renda_mensal_intermediaria = np.round(renda_mensal_intermediaria,decimals=2)
new_flux_intermediario = np.round(new_flux_intermediario,decimals=2)



SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 14

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

x = np.arange(0,t*12+1,1)
plt.style.use('seaborn-pastel')
plt.xlim([0,t*12])
plt.ylim([0,c*1.1])
fig, ax = plt.subplots(1,1,figsize=(9,9))

ax.plot(x, fluxo_caixa_invest, label=f"Investmento mensal: R\${inv}, Saldo final: R\${fluxo_caixa_invest[-1]}")
ax.plot(x, fluxo_caixa_ref, label=f"Renda mensal min: R\${r_min}, Saldo final: R\${fluxo_caixa_ref[-1]}")
ax.plot(x,new_flux_intermediario, label=f"Renda mensal intermediaria: R\${renda_mensal_intermediaria}, Saldo final: R\${new_flux_intermediario[-1]}")
ax.plot(x, new_flux_zero, label=f"Renda mensal maxima: R\${renda_mensal_zero}, Saldo final: R\${new_flux_zero[-1]}")

ax.legend(loc='lower left', frameon=False)
ax.set_title(f'Montante inicial: R\${c} , tempo = {t} anos, taxa de juros = {round(j*100,2)}% a.a')
ax.set_xlabel(f'Meses')
ax.set_ylabel(f'Reais')
ax.ticklabel_format(style='plain')

ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))

plt.savefig("Simulacao_dinheiro.png",dpi=300)
plt.show()
