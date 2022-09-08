from numpy import*

def tailleTab():
    global n
    n=0
    while n<2:
        n = int(input("Saisir N:"))
def remplirT():
    global t
    t= array([dict()]*n)
    for i in range (n):
        t[i]=dict()
        t[i]["Longeur"] = float(input("Saisir la Longeur du piece n°"+str(i+1)+": "))
        t[i]["Largeur"] = float(input("Saisir la Largeur du piece n°"+str(i+1)+": "))
        t[i]["Type"] = "X"
        while not(t[i]["Type"] in "ABC"):
            t[i]["Type"] = input("Saisir le Type du piece n°"+str(i+1)+": ").upper()
def calc():
    global maxim
    for i in range(n):
        maxim = t[0]["Longeur"]*t[0]["Largeur"]
        for i in range (1,n):
            if ((t[i]["Longeur"]*t[i]["Largeur"]) > maxim):
                maxim = t[i]["Longeur"]*t[i]["Largeur"]
    print("Maxim = "+str(maxim))
def tri():
    perm = False
    while (perm == False):
        perm=True
        for i in range(n-1):
            if(t[i]["Type"] > t[i+1]["Type"]):
                aux = t[i]
                t[i] = t[i+1]
                t[i+1] = aux
                perm = False

tailleTab()
remplirT()
calc()
print(t)
print("--------------------------------------------------")
tri()
print(t)
