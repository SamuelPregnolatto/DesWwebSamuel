containers = document.querySelectorAll('.container-img');

function atualizaAtivo(indexNovoAtivo) {
  for (let index = 0; index < containers.length; index++) {
    containers[index].classList.remove('ativo');
  }

  containers[indexNovoAtivo].classList.add('ativo');
}
