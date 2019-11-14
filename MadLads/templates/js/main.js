

/*

$(function() {
	var madStory = "One morning, about a week after Bingley's engagement with $noun$ had been formed, as he and the females of the family were sitting together in the dining-room, their attention was suddenly drawn to the window, by the sound of a carriage; and they perceived a chaise and four driving up the lawn. It was too $adjective$ in the morning for visitors, and besides, the equipage did not answer to that of any of their neighbours. The horses were post; and neither the $noun$, nor the livery of the servant who preceded it, were familiar to them. As it was certain, however, that somebody was coming, Bingley instantly prevailed on Miss Bennet to avoid the confinement of such an intrusion, and walk away with him into the $noun2$ They both set off, and the conjectures of the remaining three continued, though with little satisfaction, till the door was $verb$ open and their visitor entered. It was Lady Catherine de Bourgh."


	// hide the story from view
	$("#story").hide();

	// ---- event handler ---- //
	$("#btn-click").click(function(e) {
		var userInput = []
		// grab the values from the input boxes, then append them to the DOM
		$(".person").empty().append($("input.person").val());
		userInput.push(($("input.person").val()));

		$(".adjective").empty().append($("input.adjective").val());
		userInput.push(($("input.adjective").val()));

		$(".noun").empty().append($("input.noun").val());
		userInput.push(($("input.noun").val()));

		$(".job-title").empty().append($("input.job-title").val());
		userInput.push(($("input.job-title").val()));

		$(".noun2").empty().append($("input.plural-noun").val());
		userInput.push(($("input.noun").val()));

		$(".verb").empty().append($("input.verb").val());
		userInput.push(($("input.verb").val()));

		console.log(userInput)

		// $(".story").empty().append(story);
		// show the story
		$("#mad-story").empty().append(madStory);
		$("#story").show();

		// empty the form's values
		$(':input').val('');

		// hide the questions
		$("#questions").hide();
		return userInput;
	});



	$("#play-btn").click(function(e) {
	  $("#questions").show();
	  $("#story").hide();
	});

});
*/
$(function() {

//returns array of user input
function captureInput() {
  var userInput = [];
  var madStory = "LALALA Bla Bla Bla"

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
