$(document).on("click", ".open-modal", function(e){
     $('#Modal').load($(this).attr('href'),function(){
          tinymce.remove()
          tinymce.init({
               selector: 'textarea',
               language: 'es_MX'
          });
          $('#Modal').modal({
               show:true
          });
     });
     return false;
});