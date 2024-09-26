import math
import numpy as np
# 美式期权定价（最小二乘蒙特卡洛模拟法，LSM）
S0=100
r=0.05
sigma=0.25
T=1
I=50000
M=50
def gmb_mcs_amer(K,option='call'):
    dt=T/M
    df=math.exp(-r*dt)
    S=np.zeros((M+1,I))
    S[0]=S0
    sn=gen_sn(M,I)
    for t in range(1,M+1):
        S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*sn[t])
    if option=='call':
        h=np.maximum(S-K,0)
    else:
        h=np.maximum(K-S,0)
    V=np.copy(h)
    for t in range(M-1,0,-1):
        reg=np.polyfit(S[t],V[t-1]*dt,7)
        C=np.polyval(reg,S[t])
        V[t]=np.where(C>h[t],V[t+1]*df,h[t])
    C0=df*np.mean(V[1])
    return C0

gmb_mcs_amer(100,option='call')
1.4620120629034186
gmb_mcs_amer(110,option='put')
9.918961211536654

def gbm_mcs_dyna(K,option='call'):
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

euro_res=[]
amer_res=[]
S0=100
r=0.05
sigma=0.25
T=1
I=50000
M=50
k_list=np.arange(80.,110.1,2.)
for K in k_list:
    euro_res.append(gbm_mcs_dyna(K,option='call'))
    amer_res.append(gmb_mcs_amer(K,option='call'))
euro_res=np.array(euro_res)
amer_res=np.array(amer_res)

fig,(ax1,ax2)=plt.subplots(2,1,sharex=True,figsize=(10,6))
ax1.plot(k_list,euro_res,'b',label='european call')
ax1.plot(k_list,amer_res,'ro',label='american call')
ax1.set_ylabel('call option value')
ax1.legend()
wi=1.0
ax2.bar(k_list-wi/2,(amer_res-euro_res)/euro_res*100,wi)
ax2.set_xlabel('strike')
ax2.set_ylabel('early exercise premium in %')
ax2.set_xlim(left=75,right=125)


euro_res1=[]
amer_res1=[]
S0=100
r=0.05
sigma=0.25
T=1
I=50000
M=50
k_list=np.arange(80.,110.1,2.)
for K in k_list:
    euro_res1.append(gbm_mcs_dyna(K,option='put'))
    amer_res1.append(gmb_mcs_amer(K,option='put'))
euro_res1=np.array(euro_res1)
amer_res1=np.array(amer_res1)

fig,(ax1,ax2)=plt.subplots(2,1,sharex=True,figsize=(10,6))
ax1.plot(k_list,euro_res1,'b',label='european put')
ax1.plot(k_list,amer_res1,'ro',label='american put')
ax1.set_ylabel('put option value')
ax1.legend()
wi=1.0
ax2.bar(k_list-wi/2,(amer_res-euro_res)/euro_res*100,wi)
ax2.set_xlabel('strike')
ax2.set_ylabel('early exercise premium in %')
ax2.set_xlim(left=75,right=125)

