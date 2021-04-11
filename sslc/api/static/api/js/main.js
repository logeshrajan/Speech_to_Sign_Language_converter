$(document).ready(function(){

    $(".btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $('.column').hide();
                $('.columns').show();
                $('#gif_url').attr('src',response.gif_url);
//                $('.btn2').text(response.speech)//working;
                $("#text_msg").text(response.speech);
                $('.btn').hide();
                $('.btn1').show();
            }
        });
    });

    $(".btn1").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $('.column').hide();
                $('.columns').show();
                $('#gif_url').attr('src',response.gif_url);
//                $('.btn2').text(response.speech)//working;
                $("#text_msg").text(response.speech);
                $('.btn1').hide();
                $('.btn').show();
            }
        });
    });

});



