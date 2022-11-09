ecran = document.getElementById("txtEc");
function input(v) 
{
    ecran.value = ecran.value+v;
}

function conv() 
{
    ch = ecran.value;
    i = 0;
    puiss = ch.length-1;
    s=0;
    for (i=0; i < ch.length; i++) 
    {
        if (!isNaN(ch[i])) 
        {
            x = Number(ch[i]);    
        }
        else if (ch[i] == "a") 
        {
            x= 10;
        }
        else if (ch[i] == "b") 
        {
            x= 11;
        }
        else if (ch[i] == "c") 
        {
            x= 12;
        }
        else if (ch[i] == "d") 
        {
            x= 13;
        }
        else if (ch[i] == "e") 
        {
            x= 14;
        }
        else if (ch[i] == "f") 
        {
            x= 15;
        }
        s = s+x*Math.pow(16, puiss - i);
    }    
    alert(s)
}
function annuler() {
    ecran.value = ""
    
}