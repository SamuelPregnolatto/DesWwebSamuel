let lampada = document.getElementById('lampada');

function ligar()
{
lampada.src='luzLigada.gif';  
}
function desligar()
{
lampada.src='luzDesligada.gif';
}

function alternar()
{
if(lampada.getAttribute("src")=="luzLigada.gif")desligar();
else if(lampada.getAttribute("src")=="luzDesligada.gif")ligar();
}

function sumir()
{
document.getElementById('titulo').style.color="black";
lampada.style.display ="none";  
}

function aparecer()
{
document.getElementById('titulo').style.color="red";
lampada.style.display ="inline"; 
}

function piscar()
{
    alternar()
} setInterval(piscar)
