//masonry指令
var $grid= $('.grid').masonry({
  itemSelector: '.grid-item',
  columnWidth: '.grid-sizer',
  percentPosition: true,
	horizontalOrder: true
});
//載入imagesloaded
$grid.imagesLoaded().progress( function() {
  $grid.masonry();
}); 
//當捲動到區塊時，.grid-item加入.animation執行由小至大的動畫
function revealOnScroll() {
    var scrolled = $(window).scrollTop();
    $(".grid-item").each(function() {
        var current = $(this),
            w_height = $(window).outerHeight(),
            offsetTop = current.offset().top;
        if (scrolled + w_height - 50 > offsetTop) {
            current.addClass("animation");
        } else {
            // current.removeClass("animation");
						// 當區塊離開可視範圍內移除.animation
        }
    });
}
$(window).on("scroll", revealOnScroll);

//回到最上方
$('.top').click(function() {
    $("html, body").animate({ scrollTop: 0 }, 600);
});

// //即時搜尋
// var that = $(this);
// var Search = $("#search-style");
// $("#key-in").bind("change paste keyup", function(){
//   var value = $(this).val();
//   if (!value) {
//     Search.html("");
// 		$('.grid').masonry();
//     return;
//   }; 
//   Search.html('.grid-item:not([data-title*="' + value.toLowerCase() + '"]) {display:none;}');
// 	$('.grid').masonry();
// });

//當畫面往下捲動時，搜尋框加上.addbg 將search區塊的背景顏色變成黑色
$(window).scroll(function(evt){
	if($(window).scrollTop()>0){
    $(".search").addClass("addbg");
	}else{
		$(".search").removeClass("addbg");
  }
});

