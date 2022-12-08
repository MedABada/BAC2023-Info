function verif()
{
    nom = document.getElementById("nom").value;
    pnom = document.getElementById("pnom").value;
    age = document.getElementById("age").value;
    genreM = document.getElementById("M");
    genreF = document.getElementById("F");
    type = document.getElementById("type").value;
    if(verifnp() == false)
    {
        alert("Erreur 1: Nom ou Prenom");
        return false;
    }

    if (age>30 || age<18) 
    {
        alert("Erreur 2: Age");
        return false;
    }    

    if (!genreF.checked && !genreM.checked) 
    {
        alert("Erreur 3: Genre");
        return false;    
    }
    
    if (type != "JavaScript" && type != "Python" && type != "C") 
    {
        alert("Erreur 4: Type de Formation");
        return false;    
    }
}

function verifnp()
{
    n = nom.toUpperCase();
    p = pnom.toUpperCase();
    i = 0;
    j = 0;
    do
    {
        i++
    } 
    while(n[i]<"Z" && n[i] && (n[i]>"A") && i != n.length);
    do
    {
        j++
    } 
    while(p[j]<"Z" && p[j] && (p[j]>"A") && j != p.length);

    return(i == n.length && j == p.length);

}