$(document).ready(function() {
	// Main

	// Test code - turns p elements red on hover, then blue
	$(".post_container").click(function() {
		//$(this).hide();

		$(this).animate({left:'100px'});
		$(this).css('borderColor', 'yellow');
	});

});

