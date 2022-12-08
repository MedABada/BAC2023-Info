def cree(f):
    ch="list des etablissement de bizert"
    f.write(ch)
    f.close()

def verif(ch):
    return ch!=""

def remplir(f):
    rep="o"
    while(rep.upper()=="O"):
        ch=input("saisir un etablissement")
        while (verif(ch)==False):
            ch=input("saisir un etablissement")
        f.write("\n"+ch)
        rep=input("saisir un autre etablissement o/n")
        while(not(rep.upper() in ["O","N"])):
            rep=input("saisir un autre etablissement o/n")
    f.close()
    

def affiche(f):
    ch=f.read()
    print(ch)
    f.close()

f=open("etablissement.txt","w")
cree(f)
f=open("etablissement.txt","a")
remplir(f)
f=open("etablissement.txt","r")
affiche(f)
    