let valorPacote=0;
let totalAdicionais=0;
 
function calcularTotalViagem(){
    calcularPacote();
    calcularAdicionais();
    let totalfinal = totalAdicionais + valorPacote
    nome=document.getElementById('nome').textContent
    document.getElementById("mensagem").innerHTML = `${nome}
}
 
function calcularAdicionais(){
    totalAdicionais =0;
 
    let adicionais= document.querySelectorAll("input[name='adicionais']");
    //console.log(adicionais);
    for (let i=0; i< adicionais.length; i++)
    {
        if (adicionais[i].checked == true)
        {
            totalAdicionais = totalAdicionais + parseFloat(adicionais[i].value);
        }
    }
    alert(`adicionais: ${totalAdicionais}`);
}
 
function calcularPacote()
{
    let qtdPacotes = document.querySelectorAll("input[name='pacotes']").length;
    //console.log(qtdPacotes);
 
    let pacotes = document.querySelectorAll("input[name='pacotes']");  
    //console.log(pacotes);
 
  //let valor =  document.querySelector("input[name='pacotes']:checked").value;
    //            i < pacotes.length
    for (var i=0; i < qtdPacotes; i++)
    {
        if (   pacotes[i].checked == true    )
        {
          //  console.log(pacotes[i].value);
            valorPacote = Number(pacotes[i].value);
            break;
        }
    }
}