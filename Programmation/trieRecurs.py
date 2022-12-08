from numpy import*

def tri(t,n,i,j):
    if(j!=n):
        if(i!=n-1):
            if(t[i]<t[i+1]):
                aux = t[i]
                t[i] = t[i+1]
                t[i+1] = aux
                return(tri(t,n,i+1,j))
            else:
                return(tri(t,n,i+1,j))
        else:
            return(tri(t,n,0,j+1))

def saisitN(inf,sup):
    n = int(input("Saisir n: "))
    while not(inf<=n<=sup):
        n = int(input("Saisir n: "))
    return n

def remplir(t,n,i):
    if(n==i):
        t[i] = int(input("Saisir t["+str(i)+"]:"))
    else:
        t[i] = int(input("Saisir t["+str(i)+"]:"))
        return(remplir(t,n,i+1))

def aff(t,n):
    if n > 0:
        aff(t,n-1)
        print(t[n-1],end="|")
        
n = saisitN(3,15) 
t=array([int]*n)
remplir(t,n-1,0)
print("Avant Tri:")
aff(t,n)
tri(t,n,0,0)
print("\nApres Tri:")
aff(t,n)