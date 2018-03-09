$('#likes').click(function(){
	var postid;
	postid = $(this).attr("data-postid")
	$.get('/pethub/like',{post_id: postid}, function(data){
		$('#like').html(data);
			$('#likes').hide();
	});
});