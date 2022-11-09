from numpy import *

def saisitN():
    global n
    n=0
    while (n <2 or n>30):
        n = int(input("Saisir la taille du Tableaux:"))
def remplissage():
    global T
    T = array([str]*n)
    for i in range(n):
        T[i] = ""
        while  not(1<=len(T[i])<=5):
            T[i] = input("Saisir la chaine dans la case n°"+str(i+1)+":")
def somme():
    somme = 0
    for i in range (n):
        somme+=extraire(T[i])
    print (somme)

def extraire(ch):
    x = ""
    for i in range (len(ch)):
        if (ch[i].isdigit()):
            x = x+ch[i]
        
    ns = int(x)
    return (ns)

saisitN()
remplissage()
somme()
f1 = open ("C:\School\Programmation\Etude\SommeTab\somme.txt","w")
for i in range (n):
    f1.write(str(extraire(T[i]))+"\n")
f1.close()
    