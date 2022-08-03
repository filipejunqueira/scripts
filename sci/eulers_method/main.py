import numpy as np
import matplotlib.pyplot as plt
# Eulers Method:
# f'(x) = F(x,f(x)) and (xo,f(xo))
# f'(x) is the slope of a tangent line!
# for simplicity we will call f'(x) = y'  and f(x) = y
# y1 - y0 = m (x1 -x0)
# y = yo + F(xo,yo)*(x1-x0 )
# we call x1 - x0  the step size or h
# so what we get y = y0 + F(xo,s(xo))*h



# Define parameters
r = 1
K = 100
f = lambda t,y: r*y*(1-y/K) # ODE

h = 0.1 # Step size
max_time = 10 # Maximum time
t = np.arange(0, max_time, h) # Numerical grid
y0 = 1 # Initial Condition

# Explicit Euler Method
y = np.zeros(len(t)) #  We need to create a grid for our y or s values
y[0] = y0 # initializing our initial condition

# fitting
for i in range(0, len(t) - 1):
    y[i + 1] = y[i] + h*f(t[i], y[i])

# plotting our stuff

plt.figure(figsize = (12, 8))
plt.plot(t, y, 'bo--', label='Approximate')
plt.plot(t, y0*K*np.exp(r*t)/(K+y0*(np.exp(r*t) - 1)), 'g', label='Exact')
plt.title('Approximate and Exact Solution for the logistic growth ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()