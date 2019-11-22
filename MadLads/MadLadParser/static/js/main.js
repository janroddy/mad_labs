
//This function runs as soon as the page loads
$(document).ready(function() {
	$("#story-title").empty().append(storyName);

	$("#story").hide();
	//produceInputForms(arr);

});

//On the button click save the user input and display the story
$("#btn-click").click(function(e) {
	for (var i = 0; i < arr.length; i++) {
		var input = $("#box" + i).val();
		console.log(input)

	//add input to userInput array
		userInput.push(input);

	}
	console.log(userInput[0]);

	$("#in0").empty().append($(userInput[0]));

	// append the story to the DOM
	$("#mad-story").empty().append(madStory);
	//show the story to the user
	$("#story").show();
	// empty the form's values
	$(':input').val('');
	// hide the questions
	$("#questions").hide();


	});
//global variable to store the userInput
userInput = [];
//sample array and story for testing purposes
var storyName = "Mad Pride and Prejudice"
//arr = ["noun", "verb", "adjective", "name"]
var madStory = "One morning, about a week after Bingley's engagement with <span id='in0'></span> had been formed, as he and the females of the family were sitting together in the dining-room, their attention was suddenly drawn to the window, by the sound of a carriage; and they perceived a chaise and four driving up the lawn."

//arr is am array with they number and types of words for the user to input
function produceInputForms(str) {
	arr = str.split(',');
	for (var i = 0; i < arr.length; i++) {
		$("form").append("<label for='box" + i + "'> Enter a " + arr[i] + "</label>" + "<br>");
		$("form").append("<input id='box" + i + "'>" + "<br>");
	}
	/*
	arr.forEach(element => $("form").append("<label for=box" + count + "> Enter a " + element + "</label>" + "<br>" + "<input>" + "<br>"
		));
		*/

}
