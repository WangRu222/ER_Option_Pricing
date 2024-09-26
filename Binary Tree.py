import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family']='serif'

# 函数构造
def CRR_option_value(S0,K,T,r,sigma,otype,M=4):
    S0,K,T,r,sigma=float(S0),float(K),float(T),float(r),float(sigma)
    dt=T/M
    df=math.exp(-r*dt)
    u=math.exp(sigma*math.sqrt(dt))
    d=1/u
#     q=(math.exp(r*dt)-d)/(u-d)
    q = (math.exp(r * dt) - d) / (u - d)
    mu=np.arange(M+1)
    mu=np.resize(mu,(M+1,M+1))
    md=np.transpose(mu)
    mu=u**(mu-md)
    md=d**md
    S=S0*mu*md
    if otype=='call':
        V=np.maximum(S-K,0)
    else:
        V=np.maximun(K-S,0)
    z=0
    for t in range(M-1,-1,-1):
        V[0:M-z,t]=(q*V[0:M-z,t+1]+(1-q)*V[1:M-z+1,t+1])*df
        z+=1
    return V[0,0]

# 模型参数设置
S0=100
K=100
T=1
r=0.05
sigma=0.2
c=CRR_option_value(S0,K,T,r,sigma,otype='call',M=4)
print(c)


# S0=data['标的资产价格'][0]
# K=5.25
# T=data['剩余到期日'][0]
# r=0.015
# sigma=data['历史波动率'][0]
# CRR=[]
# for i in range(2,100):
#     m=i
#     crr_values=CRR_option_value(S0,K,T,r,sigma,otype='call',M=m)
#     CRR.append(crr_values)
# crr=pd.DataFrame({'M':range(2,100),
#     'CRR_Value':CRR})
# plt.figure(figsize=(10,8))
# plt.plot(crr['M'],crr['CRR_Value'],label='crr value')
# plt.axhline(0.1788,color='r',label='real option value')
# plt.grid()
# plt.legend()
# plt.show()
