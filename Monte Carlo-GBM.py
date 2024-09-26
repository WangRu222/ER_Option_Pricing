# 几何布朗运动的随机过程下的蒙特卡洛模拟
S0=100
r=0.05
sigma=0.25
T=1
I=50000
M=50
def gbm_mcs_dyna(K,T,S0,option='call'):
    dt=T/M
    S=np.zeros((M+1,I))
    S[0]=S0
    sn=gen_sn(M,I)
    for t in range(1,M+1):
        S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*sn[t])
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


