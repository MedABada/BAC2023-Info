from numpy import*
import random
def sPaire(t,n,i):
    if (n<i):
        return 0
    elif(t[i] % 2 == 0):
        return(t[i]+sPaire(t,n,i+1))
    else:
        return(sPaire(t,n,i+1))

n = int(input("n: "))
t = array([0]*n)
for i in range(n):
    t[i]= random.randint(-50,50)
print(sPaire(t,n-1,0))