$(function() {
	nav_li = $('#nl');
	if(nav_li.length)
	{
		//$("#moving_block").css({'left' : (parseInt(nav_li.position().left) + parseInt($('.logo_wrapper').css('margin-right'))) + 'px', 'width' : nav_li.css("width")})
		$("#moving_block").css({'left' : (parseInt(nav_li.position().left)) + 'px', 'width' : nav_li.css("width")})
		nav_font = $('#nl > a');
		nav_font.css({'color' : 'white'});
	}
	$('.nav_container .nav_button a').mouseenter(function(){
		var parent = $(this).parent();  
        left = parent.position().left;  
		if(left >= $('#cal_li').position().left)
			return;
		$('.nav_container .nav_button a').css({'color' : '#337ab7'});	
        $("#moving_block").stop(true,true).animate({left:left, width: parent.css("width")}, "fast");  
		$(this).css({'color' : 'white'});	
	});	

	//$('.nav_container li a').mouseleave(function(){
	//	chosen = $('#nl')
    //    left = chosen.position().left;  
	//	$('.nav_container li a').css({'color' : '#337ab7'});	
    //    $("#moving_block").stop(true,true).animate({left:left, width: chosen.css("width")}, "fast");  
	//	chosen.css({'color' : 'white'});	
	//});	

});
