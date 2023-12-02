function atualizaAtivo(indexNovoAtivo) {
  //Loop for para remover a classe 'ativo' do elemento, não importando em qual elemento esteja.
  for (let index = 0; index < containers.length; index++) {
    containers[index].classList.remove('ativo');
  }

  //Adicionando a classe ativo ao elemento clicado
  containers[indexNovoAtivo].classList.add('ativo');
}
window.addEventListener("scroll", function(){
  let navbar = document.querySelector('#navbar')
  navbar.classList.toggle('rolagem', window.scrollY > 0)
})

containers = document.querySelectorAll('.container-img');
