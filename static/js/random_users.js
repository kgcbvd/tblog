$(window).load(function(){
    $.getJSON('../random_users', function (data) {
        var items = [];
        $.each(data, function (key, val) {
            items.push('<li><a href="../user'+ key + '">' + val + '</a></li>');
        });
        $('<ul/>', {
            'class': 'list-unstyled', html: items.join('')
        }).appendTo('#list_users');
    });
});