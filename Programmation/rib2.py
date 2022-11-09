def saisie():
    global n
    n=input("saisie de RIB: ")
    while not(len(n)==20):
        for i in range(len(n)):
            while not("0"<n[i]<"9"):
                n=input("saisie de RIB: ")
def rib():
    global p1
    global p2
    global p3
    global p4
   
    p3=n[5:18]
    p4=n[18]+n[19]
    
def cal(n):
    s=0
    for i in range (len(n)):
        a=int(n[i])
        s=s+(a*i)
        
    while s>99:
        ch=str(s)
        s=0
        for i in range (len(ch)):
            s=s+int(ch[i])
    return s

def verif(x):
    x=int(p4)
    return cal(p3)==x
       
    
    

saisie()
rib()
print(verif(n))