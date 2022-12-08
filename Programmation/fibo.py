def fibo(n):
    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        v = 1
        w = 1
        for i in range (2,n):
            u = v+w
            v = w
            w = u
    return u
a = int(input("a: "))
print(fibo(a))