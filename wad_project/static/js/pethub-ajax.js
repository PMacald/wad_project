$(document).ready(function() {

$('.likes-button').click(function(){
	var postid;
	postid = $(this).attr("data-postid");

	

	$.get('/pethub/like/', {posts_id: postid}, function(data){
		$('.like_count[data-postid=' + postid + ']').html(data);
		//$('#likes').hide();
	});
});


});
