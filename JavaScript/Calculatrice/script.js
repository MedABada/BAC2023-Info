ecran = document.getElementById("aff");
var nb1="", nb2="", op="";

function affich(v)
{
    ecran.value = ecran.value + v;
    if (!isNaN(v)) 
    {
        if (op == "") 
        {
            nb1 = nb1 + v;   
        }
        else
        {
            nb2 = nb2 + v;
        }
    }
    else
    {
        if ( op != "") 
        {
            op = v;
        }
        else
        {
            ecran.value = "Error";
        }
    }
        
   
}

function calc() 
{
    n1 = Number(nb1);
    n2 = Number(nb2);
    if (op == "+")
    {
        ecran.value=n1+n2;
    }    
    else if (op == "-") 
    {
        ecran.value=n1-n2;
    }
    else if (op == "*") 
    {
        ecran.value=n1*n2;
    }
    else
    {
        ecran.value=n1/n2;
    }
   
}
function annuler() 
{
    nb1 = "";
    nb2 = "";
    op = "";
    ecran.value ="";
}