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
$('.only-number').keypress(function(e){
	if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
		return false;
	}
});