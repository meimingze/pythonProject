import pulp
MyProbLP = pulp.LpProblem("LPProbDemol", sense= pulp.LpMaximize)
'''
pulp.LpProblem 是定义问题的构造函数。
"LPProbDemo1"是用户定义的问题名（用于输出信息）。
参数 sense 用来指定求最小值/最大值问题，可选参数值：LpMinimize、LpMaximize 。本例 “sense=pulp.LpMaximize” 表示求目标函数的最大值。
'''
# 2.定义决策变量
x1 = pulp.LpVariable('x1', lowBound=0,upBound=7,cat='Continous')
x2 = pulp.LpVariable('x2', lowBound=0,upBound=7,cat='Continous')
x3 = pulp.LpVariable('x3', lowBound=0,upBound=7,cat='Continous')
'''
pulp.LpVariable 是定义决策变量的函数。
‘x1’ 是用户定义的变量名。
参数 lowBound、upBound 用来设定决策变量的下界、上界；可以不定义下界/上界，默认的下界/上界是负无穷/正无穷。本例中 x1,x2,x3 的取值区间为 [0,7]。
参数 cat 用来设定变量类型，可选参数值：‘Continuous’ 表示连续变量（默认值）、’ Integer ’ 表示离散变量（用于整数规划问题）、’ Binary ’ 表示0/1变量（用于0/1规划问题）。
'''
# 3. 添加目标函数
MyProbLP += 2*x1 + 3*x2 - 5*x3;
#  添加目标函数使用 “问题名 += 目标函数式” 格式。

# 4.添加约束条件
MyProbLP += (2*x1 - 5*x2 + x3 >= 10)  # 不等式约束
MyProbLP += (x1 + 3*x2 + x3 <= 12)  # 不等式约束
MyProbLP += (x1 + x2 + x3 == 7)  # 等式约束
'''
添加约束条件使用 “问题名 += 约束条件表达式” 格式。
　　约束条件可以是等式约束或不等式约束，不等式约束可以是 小于等于 或 大于等于，分别使用关键字">="、"<=“和”=="。
'''

MyProbLP.solve()
print("Status:", pulp.LpStatus[MyProbLP.status]) # 输出求解状态
for v in MyProbLP.variables():
    print(v.name, "=", v.varValue)  # 输出每个变量的最优值
print("F(x) = ", pulp.value(MyProbLP.objective))  #输出最优解的目标函数值