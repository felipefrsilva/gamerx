$('form input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length == 0) {
        console.log('sem imagem para mostrar')
    }else{
        if(arquivos[0].type == 'image/jpeg') {
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
        $('figure').prepand(imagem);
        } else {
            allert('Formato não suportado')
        }
    }
});