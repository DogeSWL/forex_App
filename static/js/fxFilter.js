$('#fxFilter').keyup(function(){
   var aValue = $(this).val().toUpperCase();

   // show all if no input in filter
   if(aValue == ""){
      $('.fxSymbols > button').show();
   } else {
      $('.fxSymbols > button').each(function(){
         var text = $(this).text().toUpperCase();

         // indexOf returns -1 if aValue not in text
         // if indexOf returns -1 hide text, else show text
         (text.indexOf(aValue) >= 0) ? $(this).show() : $(this).hide();
      });
   };
});
