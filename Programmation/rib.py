def saisit():
    global rib
    rib = ""
    ver = False
    while (ver == False):
        rib = input("saisir votre rib: ")
        ver = verifSaisit(rib)

def verifSaisit(ch):
    i = 0
    v=True
    while(i<len(ch) and v == True):
        if not("0"<=ch[i]<="9"):
            v=False
        else:
            i = i+1
    return(i == 20)

def verifRib():
    p3 = rib[5:18]
    p4 = rib[-2] 
    print( int(p4)==calcSomme(p3))
    
    
def calcSomme(x):
    n = int(x)
    res = 0
    for i in range (len(x)):
            y = int(x[i])
            res = res+(y *i)
    while res>99:
        ch=str(res)
        s=0
        for i in range(len(ch)):
            s=s+int(ch[i])
        res=s
    return res
    
saisit()
verifRib()