$('button').click(function() {

   // get value of button clicked
   var btnValue = $(this).val();

   // .val( function ): Function( Integer index, String value ) => String
   // a function returning the value to set. [this] is the current element
   // receives the index position of the element in the set and the old value as arguments.
   $('#searchText').val(function(_, searchVal){

     if (searchVal.length == 0){
       return btnValue;
     }else {
       var fxArr = searchVal.split(",");
       var btnIndex = fxArr.indexOf(btnValue);

       if(searchVal.match(btnValue)){
         fxArr.splice(btnIndex,1);
         return fxArr.toString();
         }else {
           return searchVal + "," + btnValue;
       }
     }
   });
});
