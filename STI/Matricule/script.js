mat = document.getElementById("txtMat");
nom = document.getElementById("txtNom");
date = document.getElementById("dateLoc");
nbJr = document.getElementById("nbJour");

function verif() 
{
    verif_matricule();
    verif_nom();
    verif_date();
}

function verif_matricule()
{
    if (mat.value.length == 12) 
    {   
        ch = mat.value;
        m1 = ch.substr(0,3);
        m2 = ch.substr(3,5);
        m3 = ch.substr(-4);
        
        if (!isNaN(m1) && m2.toUpperCase() == "TUNIS" && !isNaN(m3)) 
        {
            return(true);
        }
        else
        {
            alert("Jawek Moch Behi");
        }
    }
}

function verif_nom() 
{
    if (isAlpha(nom.value) == true) 
    {
        return(true);
    }
    else
    {
        alert("Esmk ma3jebnich");
    }
}

function isAlpha(ch) 
{
    if (ch.length>0) 
    {
        i=0;
        ch = ch.toUpperCase();
        if(ch[0]==" " || ch[ch.length-1]==" ")
        {
            alert("erreur");
            return false;
        }
        while ((ch[i]>="A" && ch[i]<= "Z") || ch[i]==" " && i<ch.length) 
        {
            i = i+1;      
        }    
    }
    return i == ch.length;
}

function verif_date(date) 
{
    j = Number(date.substr(0,2));
    m = Number(date.substr(3,2));
    a = Number(date.substr(6,4));

    if (!isNaN(j) && !isNaN(m) && !isNaN(a)) 
        {
            if ((j<=31 && j>=1) && (m >= 1 && m<=12) && (a>=2022))
            {
                ndate = new Date (a, m, j);
                dateRetour = new Date (ndate).setDate(nbJr);
                console.log(dateRetour);
            }
            else
            {   alert("erreur date");
                return (false);
            }
        }
    else
        {   alert("erreur date");
            return(false);
        }
    return
}