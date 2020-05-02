import numpy as np
import gmpy2

def z(i):
    file = open("local_code/junying/z.txt","r")
    a=[]
    for line in file:
        a.append(float(line.strip('\n')))
    return a[i]

def mb(i):
    file = open("local_code/junying/mb.txt","r")
    a=[]
    for line in file:
        a.append(float(line.strip('\n')))
    return a[i]

def dmb(i):
    file = open("local_code/junying/dmb.txt","r")
    a=[]
    for line in file:
        a.append(float(line.strip('\n')))
    return a[i]

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
    return 5*np.log(dL(z, o_l, o_m, H0)/10)+30

def csys(i):
    file = open("local_code/junying/csys.txt","r")
    a=[]
    for line in file:
        a.append(float(line.strip('\n')))
    return a[i]

def gaus(mean, sigma, x):
    return np.exp(-(((x-mean)/sigma)**2)/2)/sigma/np.sqrt(2*np.pi)

#Producing cinv, used in likelihood below
b=np.zeros(shape=(40,40))
for i in range(0,40):
    for j in range(0,40):
        k=40*i+j
        b[i,j]=csys(k)
for i in range(0,40):
    b[i,i]=b[i,i]+dmb(i)
cinv=np.linalg.inv(b)

def likelihood(o_l, o_m, H0, M):
    expo=0
    for i in range(0,40):
        first_term = (mb(i)-(mu(z(i),o_l, o_m, H0)+M))
        for j in range(0,40):
            expo=expo-first_term*cinv[i,j]*(mb(j)-(mu(z(j),o_l, o_m, H0)+M))/2
    return gmpy2.exp(expo)*gaus(19.23,0.042,M)
