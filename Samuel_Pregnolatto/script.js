elemento = document.getElementById("pesquisa");
elemento.addEventListener('click', async function () 
{
document.getElementById('cidade').innerText = ""
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {
        var cep = valor.replace(/\D/g, '');
        var validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var api = `https://viacep.com.br/ws/${cep}/json/`;
            let resposta = await fetch(api);
            let dados = await resposta.json();
            console.log(dados);
            document.getElementById('cidade').innerText = dados.logradouro
        }
    }
})
var soma=document.getElementById('idade').value + 30
    alert(soma);
