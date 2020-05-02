import numpy as np
import gmpy2

def E(z, o_l, o_m):
    o_k=1-o_l-o_m
    return np.sqrt(o_m*(1+z)**3+o_l+abs(o_k)*(1+z)**2)

def dL(z, o_l, o_m, H0):
    o_k=1-o_l-o_m
    inti=0
    dz=z/100
    for i in range(0,100,1):
        inti=inti+1/E(i*dz, o_l, o_m)*dz
    c=3e8
    if o_k >= 0:
        return (c/H0)*((1+z)/np.sqrt(o_k))*np.sinh(np.sqrt(o_k)*inti)
    else:
        o_k=-o_k
        return (c/H0)*((1+z)/np.sqrt(o_k))*np.sin(np.sqrt(o_k)*inti)

def mu(z, o_l, o_m, H0):
    return 5*np.log10(dL(z, o_l, o_m, H0)/10)+30

def gaus(mean, sigma, x):
    return np.exp(-(((x-mean)/sigma)**2)/2)/sigma/np.sqrt(2*np.pi)

def likelihood(o_l, o_m, H0, M):
    
    file = open("z.txt","r")
    z=[]
    for line in file:
        z.append(float(line.strip('\n')))
    file.close()    
    
    file = open("mb.txt","r")
    mb=[]
    for line in file:
        mb.append(float(line.strip('\n')))
    file.close()
    
    file = open("dmb.txt","r")
    dmb=[]
    for line in file:
        dmb.append(float(line.strip('\n')))
    file.close()
    
    file = open("csys.txt","r")
    csys=[]
    for line in file:
        csys.append(float(line.strip('\n')))
    c=np.zeros(shape=(40,40))
    for i in range(0,40):
        for j in range(0,40):
            k=40*i+j
            c[i,j]=csys[k]
    for i in range(0,40):
        c[i,i]=c[i,i]+dmb[i]
    cinv=np.linalg.inv(c)
    expo=0
    for i in range(0,40):
        for j in range(0,40):
            expo=expo-(mb[i]-(mu(z[i],o_l, o_m, H0)+M))*cinv[i,j]*(mb[j]-(mu(z[j],o_l, o_m, H0)+M))/2
    return gmpy2.exp(expo)*gaus(-19.23,0.042,M)

