bigga = 186
P = 0.25

h = 0.72


bp = (1 - P)/P

fb = (2/3) * (bigga)
wb = (bigga - fb)

K = h * fb - wb
J = bp * (wb + fb)

wa = (K + J*h) / (1 +h)
fa = J - wa

w = wa + wb
f = fa + fb

hidratacao_cal = w/f
weight = w+f
pizzas = weight/250

print(f"H2O: {w}g, F: {f}g, with {h*100}% hidration and using {P*100}% bigga {bigga}g \nADD F: {fa}g and water: {wa}g \nPizzas: #{pizzas}")


