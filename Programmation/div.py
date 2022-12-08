def div(a,b):
    if (a<b):
        return 0
    else:
        return(1+div(a-b,b))
a = int(input("a: "))
b = int(input("b: "))

print(div(a,b))
