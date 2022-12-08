function verif()
{
    nj = document.getElementById("nbjr").value;
    nom = document.getElementById("nom").value;
    pnom = document.getElementById("pnom").value;
    cin = document.getElementById("cin").value;
    genM = document.getElementById("M");
    genF = document.getElementById("F");
    optclim = document.getElementById("clim");
    opttout = document.getElementById("toutopt");
    dLoc = document.getElementById("dateLoc").value;
    type = document.getElementById("typeVoiture").value;

    if (nj<1 || nj>10)
    {
        alert("Le nombre de jours saisi n'est pas compris entre 1 et 10.");
        return false;
    }
    if (!verifch())
    {
        alert("Le nom ou le prenom saisi est incorrect");
        return false;
    }
    if ((cin == " ") || (isNaN(cin)) || (cin.length!=8))
    {
        alert("Votre CIN est incorrect.");
        return false;
    }
    if(!genM.checked && !genF.checked)
    {
        alert("Le Choix du genre est obligatoire.");
        return false;
    }
    if(!optclim.checked && !toutopt.checked)
    {
        alert("Vous devez choisir au moins une option.")
        return false;
    }
    if(!verifDate())
    {
        alert("La date saisie n'est pas valide.");
        return false;
    }
    if(type != "Ford Mustang Mach 1" && type != "Cheverolet Camaro SS" && type != "Jeep Wrangler")
    {
        alert("type de voiture n'est pas valide");
        return false;
    }

}

function verifch()
{
    i = 0;
    j = 0;
    n = nom.toUpperCase();
    p = pnom.toUpperCase();
    
    if(n != " " && p != " ")
    {
        do
        {
            i++
        }
        while(((n[i] >= "A" && n[i] <= "Z") || n[i] == " ") && i!=n.length);
        do
        {
            j++
        }
        while(((p[j] >= "A" && p[j] <= "Z") || p[j] == " ") && j!=p.length);
    }
    return(i == n.length && j == p.length);
}

function verifDate()
{
    dRet = document.getElementById("dateRet");
    a = dLoc.substr(0,4);
    m = dLoc.substr(5,2);
    j = dLoc.substr(8,2);
    DateLoc = new Date(a,m-1,j);
    DateVer = new Date();

    if(DateLoc.getFullYear() <= DateVer.getFullYear())
    {
        if(DateLoc.getMonth() <= DateVer.getMonth())
        {
            if(DateLoc.getDate() <= DateVer.getDate())
            {
                dateRetour(DateLoc,dRet);
                return true;
            }
            else
                return false;
        }
        else
        {
            return false;
        }
    }
    else
    {
        return false;
    }
}
function dateRetour(DateLoc,dRet)
{   
    nj=Number(document.getElementById("nbjr").value)
    DateLoc.setDate(DateLoc.getDate() + nj);
    dRet.innerHTML = DateLoc;
}
    
