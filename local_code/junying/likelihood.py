import numpy as np
import gmpy2

def E(z, o_l, o_m):
    '''
    define E
    '''
    o_k=1-o_l-o_m
    return np.sqrt(o_m*(1+z)**3+o_l+abs(o_k)*(1+z)**2)

def dL(z, o_l, o_m, H0):
    '''
    define dL
    '''
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
    '''
    define mu
    '''
    return 5*np.log10(dL(z, o_l, o_m, H0)/10)+30

def gaus(mean, sigma, x):
    '''
    define a gaussian function
    '''
    return np.exp(-(((x-mean)/sigma)**2)/2)/sigma/np.sqrt(2*np.pi)


def local_csys():
    '''
    read systematic error
    '''
    file = open("local_code/junying/csys.txt","r")
    csys=[]
    for line in file:
        csys.append(float(line.strip('\n')))
    file.close()
    return csys

def local_dmb():
    '''
    read mb error
    '''
    file = open("local_code/junying/dmb.txt","r")
    dmb=[]
    for line in file:
        dmb.append(float(line.strip('\n')))
    file.close()
    return dmb

#Final speedup: moving cinv out so as to minimize the number of matrix inversions
c=np.zeros(shape=(40,40))
csys_local = local_csys()
dmb_local = local_dmb()
for i in range(0,40):
    for j in range(0,40):
        k=40*i+j
        c[i,j]=csys_local[k]
for i in range(0,40):
    c[i,i]=c[i,i]+dmb_local[i]
cinv=np.linalg.inv(c)

#covariance matrix without systematic error
c2=np.zeros(shape=(40,40))
dmb_local2 = local_dmb()
for i in range(0,40):
    c2[i,i]=c2[i,i]+dmb_local2[i]
cinv2=np.linalg.inv(c2)


def likelihood(o_l, o_m, H0, M,sys=1):
    '''
    define likelihood
    sys=1 to include systematic error
    sys=0 to ignore systematic error
    '''
    
    file = open("local_code/junying/z.txt","r")
    z=[]
    for line in file:
        z.append(float(line.strip('\n')))
    file.close()    
    
    file = open("local_code/junying/mb.txt","r")
    mb=[]
    for line in file:
        mb.append(float(line.strip('\n')))
    file.close()
    
    file = open("local_code/junying/dmb.txt","r")
    dmb=[]
    for line in file:
        dmb.append(float(line.strip('\n')))
    file.close()
    
    file = open("local_code/junying/csys.txt","r")
    csys=[]
    for line in file:
        csys.append(float(line.strip('\n')))

    expo=0
    for i in range(0,40):
        first_term = (mb[i]-(mu(z[i],o_l, o_m, H0)+M))
        for j in range(0,40):
            if sys==1:
                expo=expo-first_term*cinv[i,j]*(mb[j]-(mu(z[j],o_l, o_m, H0)+M))/2
            else:
                expo=expo-first_term*cinv2[i,j]*(mb[j]-(mu(z[j],o_l, o_m, H0)+M))/2
    return gmpy2.exp(expo)*gaus(-19.23,0.042,M)
