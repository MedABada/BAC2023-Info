from random import*
from numpy import*
def saisie():
    n=int(input("n: "))
    while not(n>0):
        n=int(input("n: "))
    return n
def remplir(t,n,i):
    if(i<n):
        t[i]=int(input(f"saisie de t[{i}]"))
        remplir(t,n,i+1)
t=array([int]*10)
remplir(t,10,0)
def aff(t,n,i):
    if(i<n):
        print(t[i],end="|")
        aff(t,n,i+1)
aff(t,10,0)
def aff2(t,n):
    if(n>0):
        print(t[n-1],end="|")
        aff2(t,n-1)
        
aff2(t,10)        
