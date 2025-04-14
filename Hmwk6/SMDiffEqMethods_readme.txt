With a defined function f(x, t), we can solve the function as if it were a differential equation.
We define a step size and a range for t, calculating x at each t. There are different algorithms
that can be written for performing this type of calculation. Here, we have three examples: One
with Euler's method, one with the second-order Runge-Kutta method, and one with the fourth-order
Runge-Kutta method.

Euler simply evaluates the next x-value for the function by adding the product of the step size
and f(x, t) to the current x-value. For the Runge-Kutta method, the algorithm is more complex,
using k_1 and k_2 parameters for the second order and k_1 to k_4 for the fourth order. Higher
orders for the RK method and smaller step sizes result in longer calculation times, however the
results are also more precise.

The example code uses a step size of 0.01 (1000 steps from t=0 to t=10); feel free to adjust the
step size as you like. The graphs for the defined function within each algorithm will not be that
precise with 100 steps, and will be pretty precise for 10,000 steps.

