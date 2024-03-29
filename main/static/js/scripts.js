$(document).ready(function() {

    var baseUrl   = 'http://localhost:8000/';
    var deleteBtn = $('.delete-btn');
    var sttbtn = $('.stt-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter     = $('#filter');
    
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(document).on("keydown", "#TxtObservacoes", function () {
        var caracteresRestantes = 500;
        var caracteresDigitados = parseInt($(this).val().length);
        var caracteresRestantes = caracteresRestantes - caracteresDigitados;
    
        $(".caracteres").text(caracteresRestantes);
    });

    $(sttbtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer confirmar a ação?');

        if(result) {
            window.location.href = delLink;
        }

    });


    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(filter).change(function() {
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

});
