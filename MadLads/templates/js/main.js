$(function() {

  // event handler for button click 
  $("#btn-click").click(function(e) {
    var input = $("input").val()
    console.log(input)
    // add the value to the DOM
    $(".results").empty().append(input);
  });

});