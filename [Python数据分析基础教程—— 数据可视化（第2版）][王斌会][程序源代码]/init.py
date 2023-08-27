## -*- coding: utf-8 -*-

#基本设置
import numpy as np                           #加载数组运算包
np.set_printoptions(precision=4)             #设置numpy输出精度
import pandas as pd                          #加载数据分析包
pd.set_option('display.precision',4)         #设置pandas输出精度
import matplotlib.pyplot as plt              #加载基本绘图包

#辅助设置
plt.rcParams['font.sans-serif']=['SimHei'];   #设置中文字体为宋体['SimSun']
plt.rcParams['axes.unicode_minus']=False;     #正常显示图中正负号

#plt.figure(figsize=(5,4));                   #图形大小
#pd.set_option('display.width', 130)          #设置pandas输出宽度
#%config InlineBackend.figure_format='retina' #提高图形显示的清晰度

#from IPython.core.interactiveshell import InteractiveShell as IS
#IS.ast_node_interactivity = "all"            #多行命令一次输出

Colors=['blue','green','grey','orange','olive','red','pink','orange','yellow','red','black']
