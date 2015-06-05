$(function() {
	$('.product_href').hover(function() {
		if($(this).data('trigger') == 0)
		{	
			$('.product_href').data('trigger', 0);
			$(this).data('trigger', '1');
			$(this).trigger('click');
		}
	});

	$('.product_href').mouseleave(function() {
		//if($(this).data('trigger') == 1)
		//{
		//	$(this).data('trigger', '0');
		//		alert($(this).data('trigger'));
			//$(this).trigger('click');
		//}
	});
});
