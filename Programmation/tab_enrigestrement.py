from numpy import*

def saisit(binf,bsup):
    n=int(input("saisir n:"))
    while not(binf<n<bsup):
        n=int(input("saisir n:"))
    return n
        
def remplir(t,n):
    for i in range(n):
        t[i]=dict()
        t[i]["nom"]=input("saisir votre nom")
        t[i]["genre"]=input("saisir votre genre")
        while not(t[i]["genre"].upper() == "M" or t[i]["genre"].upper() == "F"):
            t[i]["genre"]=input("saisir votre genre")
        t[i]["moy"]=float(input("saisir votre moyenne"))
        while not(0<=t[i]["moy"]<=20):
            t[i]["moy"]=float(input("saisir votre moyenne"))
def affiche(t,n):
    for i in range(n):
        print("nom:",t[i]["nom"]," ","genre:",t[i]["genre"]," ","moyenne:",t[i]["moy"])

def trie(t,n):
    for i in range(n-1):
        x=posmax(i,t,n)
        if(x!=i):
            l=[i]
            t[i]=t[x]
            t[x]=l

def posmax(i,t,n):
    p=i
    for j in range(i+1,n):
        if(t[p]["moy"] < t[i]["moy"]):
            p = j
    return p


        
n = saisit(1,20)
t=array([{}]*n)
remplir(t,n)
print("\n")
print("Tableaux Original: ")
affiche(t,n)
trie(t,n)
print("Tableaux Triée: ")
affiche(t,n)

                        

        