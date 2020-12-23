$(".content").addClass("active");
$(".title").addClass("active");
$(".ui.table.transition").addClass("visible");
$(".visible.transition").attr("style", "display: table !important");

$("h3:contains(Client)").attr("style", "color: teal; display: inline");
$("h3:contains(Former)").attr("style", "color: #b5cc18; display: inline");
$("h3:contains(Prospects)").attr("style", "color: #21ba45; display: inline");

$("#Client").removeClass("olive").addClass("teal");
$("#Prospect").removeClass("olive").addClass("green");

$(function () {
  $("table").tablesorter();
});

$(".ui.accordion").accordion({
  animateChildren: false,
  exclusive: false, 
});

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