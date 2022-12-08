def somme(n):
    if(n==0):
        return (n)
    else:
        return (somme(n-1)+n)

def somme2(a,b):
    if(a==0):
        return (b)
    else:
        return(somme2(a-1,b)+1)
    
a = int(input("Saisir a: "))
b = int(input("Saisir b: "))
print(somme2(a,b))
