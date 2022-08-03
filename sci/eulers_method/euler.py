import numpy as np
import matplotlib.pyplot as plt

# Eulers Method:dXZ
# f'(x) = F(x,f(x)) and (xo,f(xo))
# f'(x) is the slope of a tangent line!
# for simplicity we will call f'(x) = y'  and f(x) = y
# y1 - y0 = m (x1 -x0)
# y = yo + F(xo,yo)*(x1-x0 )
# we call x1 - x0  the step size or h
# so what we get y = y0 + F(xo,s(xo))*h


def fit(par, h, max_time):
    f = lambda t, y: par["r"] * y * (1 - y / par["K"])  # ODE
    exact_f = lambda t: y0 * K * np.exp(r * t) / (K + y0 * (np.exp(r * t) - 1))

    t = np.arange(0, max_time, h)  # Numerical grid
    y0 = par["initial_value"]
    y = np.zeros(len(t))  # We need to create a grid for our y or s values
    y[0] = y0  # initializing our initial condition

    # fitting
    for i in range(0, len(t) - 1):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    # Calculating the error:
    error = np.zeros(len(t))
    for i in range(0, len(t) - 1):
        error[i] = (exact_f(t[i]) - y[i]) / exact_f(t[i])

    return y,t,exact_f,error

parameters = { "r": 1, "K": 100, "initial_value": 1}
h = 0.5
max_time = 10
y0 = parameters["initial_value"]
K = parameters["K"]
r = parameters["r"]

y,t,exact_f,error = fit(parameters,h,max_time)

plt.figure(figsize = (12, 8))


# Question 1 and 2
plt.plot(t, y, 'bo--', color = "#FF7F50", label='Approximate')
plt.plot(t, exact_f(t), color = "#40E0D0", label='Exact')
plt.errorbar(t, y, yerr=[np.zeros(len(t)),error*20], ecolor='lightgrey', elinewidth=2, capsize=0)
plt.fill_between(t, exact_f(t),y, color='#DE3163', alpha=0.1)
plt.title(f'Approximate and Exact Solution for the logistic growth ODE using dt = {h} and max time = {max_time}')
plt.xlabel('t')
plt.ylabel('X(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()