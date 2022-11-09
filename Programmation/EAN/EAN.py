from pickle import*
from numpy import*

def saisieN():
    global n
    n=0
    while not(2<=n<=30):
        n = int(input("Saisir N: "))
def remplirF():
    global ch
    global f
    f = open("code.txt","w")
    for i in range(n):
        ch = int(input("saisir ch: "))
        while verif(ch):
            ch = int(input("saisir ch: "))
        f.write(ch)
    f.close()
def verif(ch):
    i = 0
    while i<len(ch) and ('0'<=ch[i]<='9'):
        i = i+1
    return(i==len(ch) and (len(ch)==13))
def transfert():
    global T
    T = array([int]*n)
    i = 0
    f = open("code.txt","r")
    while(ch!=""):
        
saisieN()
remplirF()
transfert()
tri()
remplir2()