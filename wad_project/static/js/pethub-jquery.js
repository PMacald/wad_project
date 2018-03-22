$(document).ready(function() {
	
	
	// -- Link highlights on hover --
	$("a").hover(function() {
		$(this).toggleClass('selected');
		
		$(this).on('mouseleave', function() {
			$(this).removeClass('selected');
		});
	});
	
	// Current page link is highlighted
	var url = window.location.href;
	
	// Clean up url, remove #'s, parameters
	url = url.substring(0, (url.indexOf('#') == -1) ? url.length : url.indexOf('#'));
	url = url.substring(0, (url.indexOf('?') == -1) ? url.length : url.indexOf('?'));
	
	// Get file name if it exists
	var parts = url.split('/');
	var file_name = parts.pop() || parts.pop();   // to handle trailing slash if exists
	
	if (file_name == '') {
		url = 'index.html';
	}
	
	// 
	$('#navbarLinks a').each(function() {
		if (url == this.href) {
			$(this).addClass('activePage');
		}
	});
	
	// --
	
	// Post container expand and light up on focus
	$(".post_container").click(function() {
		
		// Deactivate previous post
		$(this).siblings(".post_container").animate({width:"70%"}, "fast");
		$(this).siblings(".post_container").css({'borderColor': 'purple', 'borderWidth' : '2px'});
		
		// Expand post		
		$(this).animate({width:"80%"});
		$(this).css({'borderColor': '#e80707', 'borderWidth': '5px'});
		
	});

});
