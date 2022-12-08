def ext(ch,n,ch2):
    if(n == 0):
        return ch2
    elif ("0"<=ch[n]<="9"):
        return(ext(ch,n-1,ch[n]+ch2))
    else:
        return(ext(ch,n-1,ch2))
ch = input("ch: ")
ch2=""
print(ext(ch,len(ch)-1,ch2))