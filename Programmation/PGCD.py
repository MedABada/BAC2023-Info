def pgcd(a,b):
    if(b==0):
        return a
    else:
        return(pgcd(b,a%b))

a = int(input("a: "))
b = int(input("b: "))
print(pgcd(a,b))