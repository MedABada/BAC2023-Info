from numpy import*
import random
def moyTab(t,n,i):
    if (n<i):
        return 0
    else:
        return(t[i]+moyTab(t,n,i+1))/2
n = int(input("n: "))
t = array([0]*n)
for i in range(n):
    t[i]= random.randint(-50,50)
print(moyTab(t,n-1,0))
