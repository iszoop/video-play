/*头像下的弹幕无缝轮播*/
function touxiang_dm() {
	var li = $('.touxiang_ew ul li');
	var x = 0;
	var y = 320;
	li.eq(0).css({
		left: x + 'px'
	});
	li.eq(1).css({
		left: y + 'px'
	});
	var time = setInterval(function() {
		x--;
		y--;
		li.eq(0).css({
			left: x + 'px'
		});
		li.eq(1).css({
			left: y + 'px'
		});
		if(x == -320) {
			x = 320;
		}
		if(y == -320) {
			y = 320;
		}
	}, 8)
}
/*banner轮播*/
function banner_lb() {
	var ul = $('.banner_img'),
		nav = $('.banner_nav li'),
		title = $('.banner_text li'),
		img_w = 440,
		x = 1,
		totalImg = 6,
		time = null;
	ul.css({
		left: -img_w + 'px'
	});
	nav.eq(0).addClass('on');
	title.eq(0).css({
		display: 'block'
	});
	time = setInterval(mov_l, 3000);
	ul.parent().hover(function() {
		clearInterval(time);
	}, function() {
		time = setInterval(mov_l, 3000);
	});
	nav.hover(function() {
		x = $(this).index();
		x++;
		ul.stop().animate({
			left: -x * img_w + 'px'
		}, 300);
		nav.eq($(this).index()).addClass('on')
			.siblings()
			.removeClass('on');
		title.eq($(this).index()).css({
				display: 'block'
			})
			.siblings()
			.css({
				display: 'none'
			});

	});

	function mov_l() {
		if(x == totalImg) {
			ul.css({
				left: '0px'
			});
			x = 1;
			nav.eq(0).addClass('on')
				.siblings()
				.removeClass('on');
			title.eq(0).css({
					display: 'block'
				})
				.siblings()
				.css({
					display: 'none'
				});
		}
		ul.animate({
			left: -x * img_w + 'px'
		}, 300);
		var y = x - 1;
		nav.eq(y).addClass('on')
			.siblings()
			.removeClass('on');
		title.eq(y).css({
				display: 'block'
			})
			.siblings()
			.css({
				display: 'none'
			});
		x++;
	}
}
/*内容区右侧轮播图*/
function Rankings_lb() {
	var ul = $('.Rankings_banner_img'),
		nav = $('.Rankings_banner_nav span'),
		img_w = 260,
		x = 1,
		time = null;
	ul.css({
		left: -img_w + 'px'
	});
	nav.eq(0).addClass('Rankings_banner_on');
	time = setInterval(mov_l, 2000);
	ul.parent().hover(function() {
		clearInterval(time);
	}, function() {
		time = setInterval(mov_l, 3000);
	});
	nav.hover(function() {
		x = $(this).index();
		x++;
		ul.stop().animate({
			left: -x * img_w + 'px'
		}, 300);
		nav.eq($(this).index()).addClass('Rankings_banner_on')
			.siblings()
			.removeClass('Rankings_banner_on');
	});
	function mov_l() {

		if(x == 4) {
			ul.css({
				left: '0px'
			});
			x = 1;
			nav.eq(0).addClass('Rankings_banner_on')
				.siblings()
				.removeClass('Rankings_banner_on');
		}
		ul.animate({
			left: -x * img_w + 'px'
		}, 300);
		var y = x - 1;
		nav.eq(y).addClass('Rankings_banner_on')
			.siblings()
			.removeClass('Rankings_banner_on');
		x++;
	}
}
