def chaine(ch):
    if len(ch)==0:
        return ""
    elif "0"<ch[len(ch)-1]<"9":
        return  chaine(ch[:len(ch)-1])+ch[len(ch)-1]
    else :
        return chaine(chaine(ch[:len(ch)-1]))
print(chaine("a141a7"))