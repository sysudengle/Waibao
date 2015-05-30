$(function() {
	$('.compute_submit').click(function(){
		var c = new Array(13);
		var e = new Array(13);
		var g = new Array(16);
		for(var i = 2; i < 13; i++)
		{
			if(i != 6)
				c[i] = parseFloat($('#c' + i).val());
			else
				c[i] = $('#c' + i).val();
		}
		//var c2 = $('#c2').val();
		//var c3 = $('#c3').val();
		//var c4 = $('#c4').val();
		//var c5 = $('#c5').val();
		//var c6 = $('#c6').val();
		//var c4 = 1;
		//var c5 = 1;
		//var c10 = 1;
		//var c11 = 1;
		//var c12 = 1;
		
//		c[2] = 30;
//		c[3] = 280;
//		c[4] = 1956;
//		c[5] = 992;
//		c[7] = 120;
//		c[8] = 0.16;
//		c[9] = 0.12;
//		c[10] = 25;
//		c[11] = 8;
//		c[12] = 5000;
//		c[6] = 'h4';
//
		e[2] = 1240000 * c[2];
		e[3] = 1000000 * c[2] / c[3];
		e[3] = e[3].toFixed(0);
		e[10] = c[10] - c[11];	// changed
		e[10].toFixed(0);
		//e[10] = c[10] * 0.8 - c[11];
		//e[11] = e[10] / 10;

		//g[10] = e[10] + e[11];
		
		//e[12] = c[12] * g[10];
		e[12] = c[12] * e[10];


		g[2] = 0.07 * e[2];
		g[2] = g[2].toFixed(0);
		g[3] = c[4] / 1000 * c[5] / 1000 * e[3];
		g[3] = g[3].toFixed(0);

		//e[6] = 'v1';
		if(c[6] == 'v1')
			e[6] = c[4] * 1;
		else if(c[6] == 'v2')
			e[6] = c[4] * 2;
		else if(c[6] == 'v3')
			e[6] = c[4] * 3;
		else if(c[6] == 'v4')
			e[6] = c[4] * 4;
		else if(c[6] == 'h3')
			e[6] = c[5] * 3;
		else if(c[6] == 'h4')
			e[6] = c[5] * 4;
		else if(c[6] == 'h5')
			e[6] = c[5] * 5;
		else if(c[6] == 'h6')
			e[6] = c[5] * 6;
		else if(c[6] == 'h7')
			e[6] = c[5] * 7;

		e[7] = g[3] / e[6] * 1000 / c[7];
		e[7] = e[7].toFixed(0);
		e[9] = g[2] * (c[8] + c[9]);
		e[9] = e[9].toFixed(0);
		g[7] = c[7] * e[6] / 3000 * 3000;
		g[7] = g[7].toFixed(0);
		g[8] = g[7] * 0.03;
		g[8] = g[8].toFixed(0);
		g[9] = (parseFloat(g[8]) + parseFloat(g[7])) / e[9] * 12;
		g[9] = g[9].toFixed(0);
		//g[10] = e[10] + e[11];
		//g[11] = e[11] * e[2] * (c[8] + c[9]);
		//g[11] = g[11].toFixed(0);
		
		//g[12] = g[10] * e[9];
		g[12] = e[9] * e[10];
		g[12] = g[12].toFixed(0);

		//g[13] = parseFloat(g[11]) + parseFloat(g[12]) + parseFloat(e[12]);
		g[13] = parseFloat(g[12]) + parseFloat(e[12]);
		g[13] = g[13].toFixed(0);
		//g[13] = g[13].toFixed(0);

		//e[14] = g[8] * g[10];
		e[14] = g[8] * e[10];

		//g[14] = parseFloat(g[7]) + parseFloat(e[14]);
		g[14] = parseFloat(g[7]) + parseFloat(e[14]);
		g[14] = g[14].toFixed(0);

		g[15] = g[13] / g[14] * 100;
		g[15] = g[15].toFixed(2);

		for(var i = 2; i < 15; i++)
		{
			write2table(e[i], 'e' + i);
		}
		for(var i = 2; i < 15; i++)
		{
			write2table(g[i], 'g' + i);
		}
		write2table(g[15] + '%', 'g' + 15);

	});	

	function write2table(data, id)
	{
		$('#' + id).html(data);	
		//alert($('#' + id).html());
		//$('#' + id).text(data);	
	};
});
