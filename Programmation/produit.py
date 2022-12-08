def prod(a,b):
    if(b==0 or a==0):
        return 0
    else:
        return(prod(a,b-1)+a)

a = int(input("a: "))
b = int(input("b: "))

print(prod(a,b))