from numpy import *
from random import *
def creationMat():
    global n
    global M
    n = int(input("Saisir la Taille du Matrice: "))
    M = array([[int] * n]*n)
    
def remplirMat():
    for i in range (n):
        for j in range (n):
            M[i,j] = randint(100,1000)
            
def transfer():
    global Tp
    global Ti
    global l
    global k
    l = 0
    k = 0
    Tp=array([int]*n*n)
    Ti=array([int]*n*n)
    for i in range(n):
        for j in range(n):
            if (M[i,j] % 2) == 0:
                Tp[l] = M[i,j]
                l=l+1
            else:
                Ti[k] = M[i,j]
                k =k+1

creationMat()
remplirMat()
print(M)
transfer()
