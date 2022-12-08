from numpy import*

def saisit(inf,sup):
    n = int(input("Saisir n: "))
    while not(inf<=n<=sup):
        n = int(input("Saisir n: "))
    return n

def remplir(t,n,i):
    if i == n-1:
        t[i] = int(input("Saisir t["+str(i)+"]: "))
    else:
        t[i] = int(input("Saisir t["+str(i)+"]: "))
        remplir(t,n,i+1)

def aff(t,n):
    if n > 0:
        aff(t,n-1)
        print(t[n-1],end="|")

def affInv(t,n):
    if n > 0:
        print(t[n-1],end="|")
        aff(t,n-1)
        
print("SAISIT N")
n= saisit(3,15)
t = array([int]*n)
print("\n")
print("REMPLISSAGE:")
remplir(t,n,0)
print("\n")
print("AFFICHAGE:")
aff(t,n)
print("\n")
print("\nAFFICHAGE INVERSE:")
affInv(t,n)