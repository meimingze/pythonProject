import sympy
from sympy import *
import numpy as np
from  scipy import  integrate
'''
求常微分方程的解析解
'''
def apply_ics(sol, ics, x, known_params):
    free_params = sol.free_symbols - set(known_params);
    eqs = [(sol.lhs.diff(x,n) - sol.rhs.diff(x,n)).subs(x,0).subs(ics) for n in range(len(ics))];
    sol_params = sympy.solve(eqs, free_params);
    sol_params = sympy.solve(eqs, free_params);
    return  sol.subs(sol_params);

sympy.init_printing();
t,omega0,gamma = sympy.symbols('t,omega_0,gamma',positive = True);
x = sympy.Function('x'); # 标记x是微分函数，非变量
ode = x(t).diff(t,2) + 2*gamma*omega0*x(t).diff(t) + omega0**2*x(t);
ode_sol = sympy.dsolve(ode) # 用diff(）和dsolve得到通解
ics = {x(0) : 1, x(t).diff(t).subs(t,0) : 0} #将初始条件与字典匹配
x_t_sol = apply_ics(ode_sol,ics,t,[omega0,gamma]);
sympy.pprint(x_t_sol)
