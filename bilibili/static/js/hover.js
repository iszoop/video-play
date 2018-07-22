/*导航*/
function header_hover(cl, d) { //鼠标浮上的元素， 要显示的元素
	var cl = $(cl);
	var d = $(d)
	$(cl).hover(function() {
		$(d).css({
			display: 'block',
		});
		$(d).stop().animate({
			opacity: 1,
			top: '42px'
		}, 500);
	}, function() {
		$(d).css({
			display: 'none',
		});
		$(d).stop().animate({
			opacity: 0,
			top: '70px'
		}, 500);
	});
}

/*游戏中心右侧鼠标悬浮效果*/
function youxi_right() {
	var li = $('.youxi_right ul li'),
		img = $('.youxi_img li');
	li.hover(function() {
		var index = $(this).index();
		img.eq(index).find('img').css({
			display: 'block'
		});
	}, function() {
		var index = $(this).index();
		img.eq(index).find('img').css({
			display: 'none'
		});
	});
}
/*删除按钮*/
function guanbi() {
	var guanbi = $('.guanbi');
	guanbi.click(function() {
		$(this).parent().remove();
	});
}

/*滚动条滚动到一定位置使其发生改变*/
function scroll(param, time, top) {

	var nav_list = $(param),
		time_c = time,
		top_c = top;
	$(window).scroll(function() {
		var t = $(window).scrollTop();
		console.log('当前滚动条的位置： '+t);
		if(t >= top_c) {
			nav_list.stop().animate({
				top: '0px'
			}, time_c);
		} else {
			nav_list.stop().animate({
				top: '200px'
			}, time_c);
		}
	});
}
/*nav_list悬浮导航点击跳转事件*/
$(function(){
	var	nav_list = $('.nav_list div'),
		x = -1,
		i = 0,
		top = $(window).scrollTop(),
		header_f_h = $('.header_f').outerHeight(),
		nav_h = $('.nav').outerHeight(),
		banner_box_h = $('.banner_box').outerHeight(),
		zhibo_box = $('.zhibo_box').outerHeight();
nav_list.click(function(){
	i = $(this).index();
	if(i!=nav_list.length-1){
		$('html, body').animate({
        scrollTop: header_f_h+nav_h+banner_box_h+i*381+10
    }, 500);
	}else{
		$('html, body').animate({
        scrollTop: 0
    }, 500);
	}
		
	});
});
/*右侧内容区鼠标悬浮*/
function Rankings_hover(box){
	var nav = $(box+' .Rankings_nav ul li'),
		li = $(box+' .Rankings_img>li');
		nav.eq(0).addClass('opacity');
		li.eq(0).css({display:'block'});
		
	nav.hover(function(){
		var index = $(this).index();
		nav.eq(index).addClass('opacity').siblings().removeClass('opacity');
		li.eq(index).css({display:'block'}).siblings().css({display:'none'});
	});
}
/*左侧内容区鼠标浮上*/
function pic_hover1(clas){
	var pic = $(clas);
	pic.hover(function(){
		$(this).children('div.mask').animate({opacity:'1'},200);
		$(this).find('p.num').animate({top:'80px'},50);
		$(this).find('.snum p').eq(0).css({color:'#00a1d6'});
	},function(){
		$(this).children("div.mask").animate({opacity:'0'},200);
		$(this).find('p.num').animate({top:'58px'},50);
		$(this).find('.snum p').eq(0).css({color:'#000'});
	});
}
/*视频预览效果*/
function pic_hover2(clas){
	var div =clas;
	$(div).mousemove(function(e){
		$(this).stop().animate({opacity:'1'},200);
		$(this).find('.shipin_top').stop().animate({opacity:'1'},500);
		$(this).find('.shipin').stop().animate({opacity:'1'},500);
    	console.log('鼠标在当前元素的X坐标： '+e.offsetX);
		var row = $(this).find('.shipin').attr('data-row'),
			sum = $(this).find('.shipin').attr('data-sum'),
			w = $(this).find('.shipin').outerWidth(),
		 	h = $(this).find('.shipin').outerHeight(),
			i = Math.floor(e.offsetX/(w/sum)),//计算当前坐标占当前总数的百分比
      		y = Math.floor(i/row),//计算每列占百分比用来判断什么时候换行
      		x = Math.floor(i-(y*row));//计算背景图x坐标
        	$(this).find('.shipin').css({'background-position': (-x*w)+'px '+' '+(-y*h)+'px'});
        	$(this).find('span').css({width:(e.offsetX/w*100)+'%'});
 		});
		$(div).mouseout(function(){
			$(this).stop().animate({opacity:'0'},0);
			$(this).find('.shipin_top').stop().animate({opacity:'0'},0);
			$(this).find('.shipin').stop().animate({opacity:'0'},0);
			$(this).find('.shipin').css({'background-position':'0px '+' '+'0px'});
			$(this).find('span').css({width:'0%'});
			
		});
}
