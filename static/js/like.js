$('#like').click(function(){
    $.ajax({
        type: "POST",
        url: "/like",
        data: {'id': $(this).attr('name'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
        dataType: "text",
        success: function(response) {
            alert('You liked this');
        },
        error: function(rs, e) {
            alert(rs.responseText);
        }
    });
});