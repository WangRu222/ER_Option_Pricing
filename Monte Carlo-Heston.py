# heston随机波动率下的蒙特卡洛模拟
S0=100
r=0.015
v0=0.001
kappa=1.5
theta=0.25
sigma=0.25
rho=0.05
T=1
corr_mat=np.zeros((2,2))
corr_mat[0,:]=[1,rho]
corr_mat[1,:]=[rho,1]
cho_mat=np.linalg.cholesky(corr_mat)
cho_mat


M=50
I=50000
def heston_mcs_dyna(K,T,S0,option='call'):
    dt=T/M
    ran_num=npr.standard_normal((2,M+1,I))
    v=np.zeros_like(ran_num[0])
    vh=np.zeros_like(v)
    v[0]=v0
    vh[0]=v0
    for t in range(1,M+1):
        ran=np.dot(cho_mat,ran_num[:,t,:])
        vh[t]=(vh[t-1]+kappa*(theta-np.maximum(vh[t-1],0))*dt+sigma*np.sqrt(np.maximum(vh[t-1],0))*np.sqrt(dt)*ran[1])
    v=np.maximum(vh,0)
    S=np.zeros_like(ran_num[0])
    S[0]=S0
    for t in range(1,M+1):
        ran=np.dot(cho_mat,ran_num[:,t,:])
        S[t]=S[t-1]*np.exp((r-0.5*v[t])*dt+np.sqrt(v[t])*ran[0]*np.sqrt(dt))
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


