
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from Packages.RK4 import *
from Packages.Configuration import *
#from Packages.Functions import *
#import Packages.Variables as Vars


# In[2]:


#Datapath=('../ebms/Config/Output/')
#Lat_bud,T_dis_bud_set1,T_dis_bud_set2,T_dis_bud_set3=np.loadtxt(Datapath+'T_bud.txt',delimiter=',')

config,configdic=importer('ForcingSteinhilber.ini')
#Vars.T=T_dis_bud_set1
data=rk4alg(BaseEquation,*config)
print(Vars.ExternalInput)

# In[3]:


#print(len(data))
plt.figure(figsize=(8,4.5))
ax=plt.subplot(111)

start=0
ax.plot(BPtimeplot(data[0][start+1:]),lna(data[2][start+1:])-data[2][200],c='b')
ax1=ax.twinx()
ax1.plot(BPtimeplot(data[0][start+1:]),Vars.ExternalOutput[0][start:],'k:')
ax1.plot(BPtimeplot(data[0][start+1:]),Vars.ExternalOutput[1][start:],'k--')
ax1.plot(BPtimeplot(data[0][start+1:]),lna(Vars.ExternalOutput[1][start:])+lna(Vars.ExternalOutput[0][start:]),'k')
ax.set_xlim(-9800,200)
ax.set_ylim(-0.85,0.25)
ax.set_ylabel('Temperature variations [°C]')
ax.set_xlabel('Time [Years]')
ax1.set_ylim(0.8,-3.1)
ax1.set_ylabel('Volcanic Forcing [$Wm^{-2}$]')

#ax.set_xscale('log')
#ax1.set_xscale('log')
#print(Vars.External)
plt.savefig('Plots/ForcingSteinhilber.png', format='PNG', dpi=400, bbox_inches='tight')
plt.show()

