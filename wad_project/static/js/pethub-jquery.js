$(document).ready(function() {
	// Main
	

	// Test code - turns p elements red on hover, then blue
	$(".post_container").click(function() {
		$(this).css('color', 'red');
	},
	function() {
		$(this).css('color', 'blue');
	});
});

