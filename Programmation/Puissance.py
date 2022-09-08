from numpy import*

def saisieN():
    global n
    n = 0
    while(n<2):
        n = int(input("N: "))
def rempliT(t,n):
    for i in range(n):
        t[i]=int(input("T["+str(i)+"]"))
def Puiss(x):
    i=2
    nb=0
    test=False
    while (x>1 and test == False):
        if x%i ==0:
            nb=nb+1
            x=x//2
            test=(nb>=2)
        else:
            i=i+1
            nb=0
    return test==True
def affiche(t,n):
    for i in range(n):
        if(Puiss(t[i])):
            print(t[i])
        
n=0
saisieN()
t = array([int]*n)    
rempliT(t,n)
print(Puiss(27))
affiche(t,n)