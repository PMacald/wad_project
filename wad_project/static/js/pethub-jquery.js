$(document).ready(function() {
	// Main
<<<<<<< HEAD

	// Test code - turns p elements red on hover, then blue
	$(".post_container").click(function() {
		//$(this).hide();

		$(this).animate({left:'100px'});
		$(this).css('borderColor', 'yellow');
=======

	// Hide navbar on scroll
	$(window).scroll(function() {
		var i = $(window).scrollTop();
		if (i >= 100) {
			$("#navbar").fadeOut("fast");
		} else {
			$("#navbar").fadeIn("fast");
		}
	});


	// Post container expand and light up on focus
	$(".post_container").click(function() {
		// Deactivate previous post
		$(".post_container").animate({width:"70%"}, "fast");
		$(".post_container").css({'borderColor': 'purple', 'borderWidth' : '2px'});

		// Expand post		
		$(this).animate({width:"80%"});
		$(this).css({'borderColor': 'yellow', 'borderWidth': '5px'});
>>>>>>> 4c27bcd42d17d6642b7c1ad9f47527dbf57a30e7
	});

});

														