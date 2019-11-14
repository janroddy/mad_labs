$(function() {

//returns array of user input
function captureInput() {
  var userInput = [];
  var madStory = "One morning, about a week after Bingley's engagement with $noun$ had been formed, as he and the females of the family were sitting together in the dining-room, their attention was suddenly drawn to the window, by the sound of a carriage; and they perceived a chaise and four driving up the lawn."

  	// hide the story from view
	$("#story").hide();

	// ---- event handler ---- //
	$("#btn-click").click(function(e) {		
		
		// grab the values from the input boxes, then append them to the DOM
		$(".box1").empty().append($("input.box1").val());
		userInput.push(($("input.box1").val()));

		$(".box2").empty().append($("input.box2").val());
		userInput.push(($("input.box2").val()));

		$(".box3").empty().append($("input.box3").val());
		userInput.push(($("input.box3").val()));
		

		// $(".story").empty().append(story);
		// show the story
		
		$("#mad-story").empty().append(madStory);
		$("#story").show();

		// empty the form's values
		$(':input').val('');

		// hide the questions
		$("#questions").hide();
		

	});

  return userInput;
}




var userIn = captureInput();
console.log(userIn)


	$("#play-btn").click(function(e) {
		$("#questions").show();
		$("#story").hide();
	});

});
