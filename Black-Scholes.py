# BSM模型
# Black-Scholes-Merton (1973) European Call & Put Valuation
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import quad
mpl.rcParams['font.family'] = 'serif'
from scipy.stats import norm

#欧式看涨期权函数
# 欧式看涨期权
def BSM_call_value(St, K, t, T, r, sigma):
    d1=(np.log(St/K)+(r+0.5*sigma**2)*(T-t))/(sigma*np.sqrt((T-t)))
    d2=d1-sigma*np.sqrt((T-t))
    return St*norm.cdf(d1)-K*np.exp(-r*(T-t))*norm.cdf(d2)
#欧式看跌期权函数
def BSM_put_value(St, K, t, T, r, sigma):
    d1=(np.log(St/K)+(r+0.5*sigma**2)*(T-t))/(sigma*np.sqrt((T-t)))
    d2=d1-sigma*np.sqrt((T-t))
    return K*np.exp(-r*(T-t))*norm.cdf(-d2)-St*norm.cdf(-d1)

# 例子
St=100
K=98
T=1
t=0
r=0.015
sigma=0.25
call=BSM_call_value(St, K, t, T, r, sigma)
put=BSM_put_value(St, K, t, T, r, sigma)
print('看涨期权价格',call,'看跌期权价格',put)
