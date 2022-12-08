def disq(a,b):
    global j
    print("Deplacement: ",j,end=" | ")
    print(a," ---> ",b)
    j+=1
def hanoi(n,d,a,i):
    if(n==1):
        disq(d,a)
    else:
        hanoi(n-1,d,i,a)
        disq(d,a)
        hanoi(n-1,i,a,d)
j=1
n= int(input("Nb disques: "))
hanoi(n,"t1","t3","t2")
