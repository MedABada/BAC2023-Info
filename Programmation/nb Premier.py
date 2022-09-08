from numpy import*

def prm(y):
    i = 2
    test=True
    while(i<=(y//2) and test):
        i=i+1
        test=(y%i != 0)
    return test

def remplirT():
    global t,n
    for i in range (n):
        t[i] = int(input("T["+str(i)+"]: "))
    
def saisieN():
    global n
    n = 0
    while(n<2):
        n = int(input("N: "))
def remplirTp(t,n,tp):
    j = 0
    for i in range(n):
        if(prm(t[i])):
            tp[j] = t[i]
            j = j+1
    return  tp,j
def afficher(t,n):
    for i in range(n):
        print(str(t[i]) +"\t")
        
        
saisieN()  
t=array([int]*n)
tp=array([int]*n)
remplirT()
tp,j=remplirTp(t,n,tp)
afficher(t,n)
afficher(tp,j)


