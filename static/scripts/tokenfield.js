$(document).ready(function () {
  /* Inicializa o campo de entrada com o plugin tokenfield (Bootstrap) para autocomplete */
  $('#tokenfield').tokenfield({
    autocomplete: {
      source: ['egg', 'tomato', 'beef steak', 'potato'], // Lista de sugestões de ingredientes para o autocomplete
      delay: 100 // Define o atraso (em milissegundos) antes de mostrar as sugestões
    },
    showAutocompleteOnFocus: true // Mostra o autocomplete assim que o campo de entrada é focado
  })

  let list_recipe = []; // Cria um array para armazenar a lista de ingredientes

  /* Obtém o valor do primeiro campo de entrada (valor inicial) */
  list_recipe[0] = $('INPUT').val();

  /* Adiciona um novo ingrediente à lista quando o usuário cria um token */
  $('INPUT').on('tokenfield:createtoken', function (e) {
    list_recipe.push(e.attrs.value); // Adiciona o ingrediente à lista
    filter(list_recipe); // Chama a função de filtragem para buscar as receitas
  })

  /* Remove um ingrediente da lista quando o usuário remove um token */
  $('INPUT').on('tokenfield:removedtoken', function (e) {
    list_recipe.splice(list_recipe.indexOf(e.attrs.value), 1); // Remove o ingrediente da lista
    filter(list_recipe); // Chama a função de filtragem para atualizar a lista de receitas
  })

  /* Função para buscar as receitas que correspondem aos ingredientes informados */
  function filter(list_recipe) {
    $('#recipe').empty(); // Limpa a área onde as receitas serão exibidas
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8000/api/match_recipe/', // URL da API que retorna as receitas
      contentType: 'application/json', // Define o tipo de conteúdo da requisição como JSON
      data: JSON.stringify({ 'listIngredient': list_recipe }), // Envia a lista de ingredientes para a API
      success: function (res) { // Quando a requisição for bem-sucedida
        if (res.length === 0) {
          // Se nenhuma receita for encontrada, exibe uma mensagem
          $('#recipe').append('<h5 style="padding-left: 23px;" class="card-text">No results were found. Try another search </h5>');
        }

        /* Loop para exibir as receitas encontradas */
        for (let idx = 0; idx < res.length; idx++) {
          // Adiciona um novo bloco para cada receita encontrada
          $('#recipe').append('<div class="col-md-6">' +
            '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
            '<div class="col-auto">' +
            '<img class="card-img-top" src=' +
            res[idx].img_url +
            ' alt="recipe">' +
            '</div>' +
            '<div class="col p-4 d-flex flex-column position-static">' +
            '<strong class="d-inline-block mb-2 text-primary">' +
            res[idx].name +
            '</strong>' +
            '<h3 class="mb-0">Ingredients</h3><ul class="Ingredients"></ul><h3 class="mb-0">Directions</h3>' +
            '<ul class="list-group list-group-flush Directions"></ul>' + '</div></div></div></div>');
          
          /* Exibe os ingredientes da receita */
          for (let ingredient of res[idx].ingredients) {
            $('.Ingredients').append('<li class="mb-1 text-muted">' +
              ingredient + '</li>');
          }
          
          /* Exibe as instruções da receita */
          for (let direction of res[idx].directions) {
            $('.Directions').append('<li class="list-group-item">' +
              direction + '</li>'
            );
          }
        }

      }
    })
  }
});
