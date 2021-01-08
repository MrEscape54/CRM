$(".content").addClass("active");
$(".title").addClass("active");
$(".ui.table.transition").addClass("visible");
$(".visible.transition").attr("style", "display: table !important");

$("h3:contains(Client)").attr("style", "color: teal; display: inline");
$("h3:contains(Former)").attr("style", "color: #b5cc18; display: inline");
$("h3:contains(Prospects)").attr("style", "color: #21ba45; display: inline");
$("h3:contains(Account Contacts)").attr("style", "color: teal; display: inline");
$("h3:contains(Vendor Contacts)").attr("style", "color: #b5cc18; display: inline");
$("h3:contains(Closed Won)").attr("style", "color: #21ba45; display: inline");




$("#Client").removeClass("olive").addClass("teal");
$("#Prospect").removeClass("olive").addClass("green");
$("#vendor-contact").removeClass("teal").addClass("olive");
$("#6-closed-won").removeClass("olive").addClass("green");


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

//Number format only works on input type: text
$("#id_opp-amount").attr("type", "text"); 

var cleave = new Cleave("#id_opp-amount", {
  numeral: true,
  numeralThousandsGroupStyle: "thousand",
});
