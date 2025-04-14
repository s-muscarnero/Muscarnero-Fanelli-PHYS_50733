def Euler(x, t, step_size, func_1): 
    return step_size*func_1(x, t)

def RK_2(x, t, step_size, func_1): 
    k_1 = step_size*func_1(x, t)
    k_2 = step_size*func_1(x+k_1/2, t+step_size/2)
    return k_2

def RK_4(x, t, step_size, func_1): 
    k_1 = step_size*func_1(x, t)
    k_2 = step_size*func_1(x+k_1/2, t+step_size/2)
    k_3 = step_size*func_1(x+k_2/2, t+step_size/2)
    k_4 = step_size*func_1(x+k_3, t+step_size)
    return ((1/6)*(k_1+2*k_2+2*k_3+k_4))