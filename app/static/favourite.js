window.onload = () => {

    $('.wrap').on('click', 'div', function () {
        const url = '/removetofav/' + $(this).index();
        window.fetch(url).then(response => response.json())
        .then(data => {
            window.location.reload(false);
        });
    });

};
