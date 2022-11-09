function verif() 
{
    nom = document.getElementById("nom").value;
    sport = document.getElementsByName("sport");
        if (!isAlpha(nom))
        {
            alert(nom+" n'est pas alphabetique");
            return false;   
        }
    
    if (!(sport[0].checked && sport[1].checked && sport[2].checked) )
    {
        alert("Sport non choché");
        return false;
    }
}

function isAlpha(ch) 
{
    i=0;
    ch = ch.toUpperCase();
    while (ch[i]>="A" && ch[i]<= "Z" && i<ch.length) 
    {
         i = i+1;      
    }    
    return i == ch.length;
}