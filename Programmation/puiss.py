def puiss(a,b):
    if (a==0):
        return 0
    elif(b==0):
        return 1
    elif(b>0):
        return(puiss(a,b-1)*a)
    else:
        b = -b
        p = puiss(a,b-1)*a
        return(1/p)
a = int(input("a: "))
b = int(input("b: "))

print(puiss(a,b))