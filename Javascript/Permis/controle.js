
perm = document.getElementById("Nperm");
nom=document.getElementById("nom");
prenom=document.getElementById("pnom");
genre=document.getElementsByName("genre");
function verif1() 
{p1=perm.value.substr(0,2);
 p2=perm.value.substr(3);
 if(perm.value.length!=8 ||isNaN(p1) || isNaN(p2) ||perm.value[2]!="/")
    {
        alert("erreur permis");
        return false;
    }
 if(nom.value=="" || !isAlpha(nom.value))
    {
        alert("erreur nom");
        return false;
    }
 if(prenom.value=="" || !isAlpha(prenom.value))
    {
        alert("erreur prenom");
        return false;
    }
 if(!genre[0].checked && !genre[1].checked)
 {
    alert("cocher le genre");
    return false;
}
}

function isAlpha(ch)
{
    ch=ch.toUpperCase();
    i=0;
    while(i<ch.length && ch[i]>="A" && ch[i]<="Z")
        i++;
    return i==ch.length;
}