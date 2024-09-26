# 跳跃扩散下的蒙特卡洛模拟
S0=100
r=0.015
sigma=0.15
lamb=0.25
mu=-0.45
delta=0.35
rj=lamb*(math.exp(mu+0.5*delta**2)-1)
T=1
def merton_mcs_dyna(K,T,S0,option='call'):
    M=50
    I=10000
    dt=T/M
    S=np.zeros((M+1,I))
    S[0]=S0
    sn1=npr.standard_normal((M+1,I))
    sn2=npr.standard_normal((M+1,I))
    poi=npr.poisson(lamb*dt,(M+1,I))
    for t in range(1,M+1,1):
        S[t]=S[t-1]*(np.exp((r-rj-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*sn1[t])+(np.exp(mu+delta*sn2[t])-1)*poi[t])
        S[t]=np.maximum(S[t],0)
    if option=='call':
        hT=np.maximum(S[-1]-K,0)
    else:
        hT=np.maximum(K-S[-1],0)
    C0=math.exp(-r*T)*np.mean(hT)
    return C0

# mape
mape=np.mean(np.abs((pred-label)/label))
# rmse
rmse=np.sqrt(np.mean(np.square(pred-label)))
# mae
mae=np.mean(np.abs(pred-label))

#MSE
mse=np.sum((label-pred)**2)/len(pred)

