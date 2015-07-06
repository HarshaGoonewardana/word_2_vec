$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/ajaxhandler',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				
				$("#result").text(response["result"]);
			},
			error: function(error){
				console.log("error");
			}
		});
	});
});
