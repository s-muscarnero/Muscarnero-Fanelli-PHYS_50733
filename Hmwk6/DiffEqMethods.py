# Euler's Method
import numpy as np
import matplotlib.pyplot as plt

# Define evaluated function and step size
from DiffEqAlgos import Euler
step_size = 10/1000
def func_1(x, t): 
    return -x**3+np.sin(t)

# Step size of 0.01 for 1000 steps from 0 to 10
tpoints = np.arange(0, 10.01, 0.01)
xpoints = []     # Define x list here
x = 0     # To avoid error of x not being defined, define x here with its initial value

# Calculate x at each t
for t in tpoints: 
    x += Euler(x,t,step_size,func_1)
    xpoints.append(x)
    
# Plot the graph of the points
plt.figure(figsize=(10, 7.5))
plt.plot(tpoints, xpoints, c = 'navy')
plt.title("x as a Function of t using Euler's Method", size = 18)
plt.xlabel("t", size = 15)
plt.ylabel("x(t)", size = 15)
plt.show()



# Second Order Runge-Kutta Method
# Define evaluated function and step size
from DiffEqAlgos import RK_2
step_size = 10/1000
def func_1(x, t): 
    return -x**3+np.sin(t)

# Step size of 0.01 for 1000 steps from 0 to 10
tpoints = np.arange(0, 10.01, 0.01)
xpoints = []     # Define x list here
x = 0     # To avoid error of x not being defined, define x here with its initial value

# Calculate x at each t
for t in tpoints: 
    x += RK_2(x, t, step_size, func_1)
    xpoints.append(x)
    
# Plot the graph of the points
plt.figure(figsize=(10, 7.5))
plt.plot(tpoints, xpoints, c = 'darkgreen')
plt.title("x as a Function of t using the Runge-Kutta Method", size = 18)
plt.xlabel("t", size = 15)
plt.ylabel("x(t)", size = 15)
plt.show()



# Fourth Order Runge-Kutta Method
from DiffEqAlgos import RK_4
step_size = 10/1000
def func_1(x, t): 
    return -x**3+np.sin(t)

# Step size of 0.01 for 1000 steps from 0 to 10
tpoints = np.arange(0, 10.01, 0.01)
xpoints = []     # Define x list here
x = 0     # To avoid error of x not being defined, define x here with its initial value

# Calculate x at each t
for t in tpoints: 
    x += RK_4(x, t, step_size, func_1)
    xpoints.append(x)
    
# Plot the graph of the points
plt.figure(figsize=(10, 7.5))
plt.plot(tpoints, xpoints, c = 'maroon')
plt.title(f"x as a Function of t using the Fourth-order Runge-Kutta Method ({10/step_size} steps)", size = 18)
plt.xlabel("t", size = 15)
plt.ylabel("x(t)", size = 15)
plt.show()