import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import pandas as pd

def make_colors(n, colormap=plt.cm.Spectral):
    return colormap(np.linspace(0.1, 1.0, n))

def make_explode(n):
    explodes = np.zeros(n)
    explodes[0] = 0.15
    return explodes

pd.set_option('display.float_format', lambda x: '%.2f' % x)

plt.rcParams["figure.figsize"] = (14,8)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2
plt.rcParams["axes.grid"] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["axes.formatter.limits"] = -10000, 10000

sp500 = fdr.StockListing('S&P500')
sp500.head(10)
