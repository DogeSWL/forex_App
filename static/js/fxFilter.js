$('#fxFilter').keyup(function(){
   var aValue = $(this).val().toUpperCase();
    if(aValue == ""){
        $('.fxSymbols > button').show();
    } else {
        $('.fxSymbols > button').each(function(){
            var text = $(this).text().toUpperCase();
            (text.indexOf(aValue) >= 0) ? $(this).show() : $(this).hide();
        });
   };
});
