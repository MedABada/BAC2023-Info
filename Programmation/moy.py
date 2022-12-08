from numpy import*
import random
def moy(t,n,i,s):
    if (i>n):
        return s/(n+1)
    else:
        return(moy(t,n,i+1,s+t[i]))
    

n = int(input("n = "))
t = array([0]*n)
for i in range(n):
    t[i]= random.randint(-50,50)
print(moy(t,n-1,0,0))


