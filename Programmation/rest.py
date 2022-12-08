def reste(a,b):
    if(a==0):
        return 0
    elif(a<b):
        return a
    else:
        return(reste(a-b,b))
a = int(input("a: "))
b = int(input("b: "))

print(reste(a,b))

