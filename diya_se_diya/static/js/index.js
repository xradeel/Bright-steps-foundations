$(".next").on("click",function(e){
    e.preventDefault();
    $(".d_purpose").hide();
    $("#personal_info").show();
  })
jQuery(".next1").on("click",function(e){
    e.preventDefault();
    jQuery(".payment_info").show();
    jQuery("#personal_info").hide();

  })
jQuery(".next2").on("click",function(e){
    e.preventDefault();
    jQuery(".payment_info").hide();
    // alert("Thank you for your Donation");
    jQuery(".d_purpose").show();

  })

$(".home_li").mouseover(function(){
    $(".home_text").hide();
    $(".home_icon").show();
});
$(".home_li").mouseout(function(){
    $(".home_text").show();
    $(".home_icon").hide();
});

$(".reg_li").mouseover(function(){
    $(".reg_text").hide();
    $(".reg_icon").show();
});
$(".reg_li").mouseout(function(){
    $(".reg_text").show();
    $(".reg_icon").hide();
});

$(".help_li").mouseover(function(){
    $(".help_text").hide();
    $(".help_icon").show();
});
$(".help_li").mouseout(function(){
    $(".help_text").show();
    $(".help_icon").hide();
});
$(".about_li").mouseover(function(){
    $(".about_text").hide();
    $(".about_icon").show();
});
$(".about_li").mouseout(function(){
    $(".about_text").show();
    $(".about_icon").hide();
});