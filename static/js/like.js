$('#like').click(function(){
    $.ajax({
        type: "POST",
        url: "like/",
        data: {'id': $(this).attr('name'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
        dataType: "text",
        success: function(likes_count) {
            if (likes_count != 0) {
                $("#rating").html(likes_count);
            }
        },
        error: function(rs, e) {}
    });
});