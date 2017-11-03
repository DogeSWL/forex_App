$('button').click(function() {

   // get value of button clicked
   var btnValue = $(this).val() + ",";

   // .val( function ): Function( Integer index, String value ) => String
   // a function returning the value to set. [this] is the current element 
   // receives the index position of the element in the set and the old value as arguments.
   $('#searchText').val(function(_, searchVal){
      if (searchVal.match(btnValue)){
         return searchVal.replace(btnValue, "");
      }
      return searchVal+ btnValue
   });
});
