from pickle import *

def remplir():
    global F
    F = open("bit.dat","wb")
    rep = 1
    while(rep == 1):
        e = saisie_bit()
        dump(e,F)
    f.close()
        

remplir()
regroup(F,F2)
afficher(F2)

