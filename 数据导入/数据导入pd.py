# Pandas 输入输出函数的说明文档 https://pandas.pydata.org/pandas-docs/stable/reference/io.html
1.
# pandas读取EXCEL文件
# Pandas 使用 read_excel() 函数读取 Excel文件。
import pandas as pd
io = ' '      # 文件名称
pd.read_excel(io, sheetname=0,header=0,index_col=None,names=None)
'''
io ： 文件路径（包括文件名）。
**header ：指定作为列名的行。**默认为 0，即首行为标题行。设置 header=None，表示无标题行，首行就是数据行。
**sheetname：指定工作表。**默认为 sheetname=0。设置 sheetname=None 返回全表， 设置 sheetname=[0,1] 返回多表 。
index_col ：指定作为行索引的列编号或列名。
names：指定列名， 类型为 list。
'''
2.
# pandas读取csv文件
# Pandas 使用 pandas.read_csv() 函数读取 Excel文件。
filepath = ''
pd.read_csv( filepath ,sep=',' , header='0', names=None, index_col=None)
'''
filepath ： 文件路径（包括文件名）。
**sep：指定分隔符。**默认为逗号 ‘,’，可根据需要设置其它分隔符。
**header ：指定作为列名的行。**如果文件没有列名则默认为 0，表示首行就是数据行；设置 header=None，表示无标题行，首行就是数据行。
index_col ：指定作为行索引的列编号或列名。
names：指定列名， 类型为 list。
'''
3.
# pandas读取文本文件
# 对于文本文件 .txt 和 .dat，可以使用 pandas.read_table() 函数读取
pd.read_table( filepath ,sep='/t', header='infer', names=None, index_col=None)
'''
filepath ： 文件路径（包括文件名）。
**sep：指定分隔符。**默认为 tab 制表符，可根据需要设置其它分隔符。
**header ：指定作为列名的行。**如果文件没有列名则默认为 0，表示首行就是数据行；设置 header=None，表示无标题行，首行就是数据行。
index_col ：指定作为行索引的列编号或列名。
names：指定列名， 类型为 list。
'''
