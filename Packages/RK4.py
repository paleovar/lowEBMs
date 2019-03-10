
# coding: utf-8

# In[7]:


from Packages.BaseEquation import *
from Packages.Functions import *
import numpy as np
import builtins
import time

def rk4alg(func,EQparam,rk4input,funccomp,var):
    #Start the runtime tracker
    Vars.start_time = time.time()
    #locally defining rk4input parameters
    n,h=num_of_integration,builtins.stepsize_of_integration
    
    #Creating an array of the variables t,T,Lat,T_global which will be the outputarray
    data=np.array([[0]*(n+1)]*3 )
    #Filling data with intitial conditions at positions data[.][0]
    data=nal(data)
    data[0][0]=var[0] #time t
    data[1][0]=var[1] #Temperature T
    data[2][0]=var[2] #Global mean temperature T_global
    
    ###Running runge Kutta 4th order n times###
    j=0
    for i in range(1, n + 1):  
        #Calculating increments at 4 positions from the energy balance equation (func)
        T0=Vars.T
        k1 = h * func(EQparam,funccomp)
        builtins.Runtime_Tracker += 1
        Vars.T=T0+0.5*k1
        k2 = h * func(EQparam,funccomp)
        builtins.Runtime_Tracker += 1
        Vars.T=T0+0.5*k2
        k3 = h * func(EQparam,funccomp)
        builtins.Runtime_Tracker += 1
        Vars.T=T0+k3
        k4 = h * func(EQparam,funccomp)
        builtins.Runtime_Tracker += 1
        
        #filling output array "data" with values from the generated increments
        #For the time simply adding the integration stepsize
        Vars.t = Vars.t + h
        if (i) % ReadoutStep == 0: 
            j += 1       
            data[0][j] = Vars.t 
            #The Temperature is an average over the generated increments
            data[1][j] = Vars.T = T0 + (k1 + k2 + k2 + k3 + k3 + k4) / 6  
            #The globalmeantemp calculated from the new generated temperature distribution
            if latitude_stepsize>0:
                data[2][j] = Vars.T_global = globalmeantemp()
            else: #if 0 dimensional
                data[2][j] = Vars.T_global = Vars.T
        #Check if the equilibrium condition is fulfilled. If true, break the loop, cut the output array to
        #the current length and move on to return the output data
        if Condition==True:
            if Runtime_Tracker > 4*ConditionLength:
                if SteadyStateConditionGlobal(data[2][j-ConditionLength:j])==True:
                    for l in range(len(data)):
                        data[l]=data[l][:(j+1)]
                    for m in range(len(Vars.Read)):
                        Vars.Read[m]=Vars.Read[m][:(j)]
                    break
    print(j)
    dataout=[data[0][:(j+1)],data[1][:(j+1)],data[2][:(j+1)]]
    return dataout

