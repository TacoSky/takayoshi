/*
 parallax
*/
$(function() {

    $('#main-base').scroll(function(){
        /* scroll valu */
        var scroll = $(this).scrollTop();
        $('#wind-base').scrollTop(scroll/4);
    });

});