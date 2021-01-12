$(".content").addClass("active");
$(".title").addClass("active");
$(".ui.table.transition").addClass("visible");
$(".visible.transition").attr("style", "display: table !important");

$("#Client").removeClass("olive").addClass("teal");
$("#Prospect").removeClass("olive").addClass("green");

$("#vendor-contact").removeClass("teal").addClass("olive");

$("#1-negotiationreview").removeClass("olive").addClass("blue");
$("#5-identification").removeClass("olive").addClass("yellow");
$("#3-under-analysis").removeClass("olive").addClass("teal");
$("#2-price-quote").removeClass("olive").addClass("grey");
$("#6-closed-won").removeClass("olive").addClass("green");
$("#7-closed-lost").removeClass("olive").addClass("red");


$(function () {
  $("table").tablesorter();
});

$(".ui.accordion").accordion({
  animateChildren: false,
  exclusive: false, 
});

$(".selection.dropdown").dropdown();
$(".ui.checkbox").checkbox();

$(".message .close").on("click", function () {
  $(this).closest(".message").transition("fade");
});

//Phone number format CLEAVE
var phoneCollection = document.getElementsByClassName("input-phone");
var phones = Array.from(phoneCollection);

phones.forEach(function (phone) {
  new Cleave(phone, {
    phone: true,
    phoneRegionCode: "{country}",
  });
});
