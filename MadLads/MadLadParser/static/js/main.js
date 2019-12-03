var str = "";
userInput = [];

//This function runs as soon as the page loads
$(document).ready(function() {

	$("#story").hide();

	$.ajax({
			url: '/get',
			type: 'get', // This is the default though, you don't actually need to always mention it
			success: function(data) {
				console.log(data)
				 produceInputForms(data);
			},
			failure: function(data) {
					alert('Got an error dude');
			}
	});
});

//On the button click save the user input and display the story
$("#btn-click").click(function(e) {
	arr = getStr().split(',');
	userInput = new Array(arr.length);
	for (var i = 0; i < arr.length; i++) {
		var input = $("#box" + i).val();
		userInput[i] = input;
	//add input to userInput array
	}
	userInput = userInput.join();
	console.log(userInput)
	$.ajax({
	    url: '/send/',
	    type: 'post', // This is the default though, you don't actually need to always mention it
			data: {
				'UserInput': userInput
			},
	    success: function(data) {
	       console.log(data);
	    },
	    failure: function(data) {
	        alert('Got an error dude');
	    }
	});
	$.ajax({
	    url: '/show',
	    type: 'get', // This is the default though, you don't actually need to always mention it
	    success: function(data) {
	       //console.log(data);
				 produceStory(data);
	    },
	    failure: function(data) {
	        alert('Got an error dude');
	    }
	});
});

function produceInputForms(str) {
	setStr(str);
	arr = str.split(',');
	for (var i = 0; i < arr.length; i++) {
		$("form").append("<label for='box" + i + "'> Enter a " + arr[i] + "</label>" + "<br>");
		$("form").append("<input id='box" + i + "'>" + "<br>");
	}
}

	//THIS STUFF IS ADDED BY KODY AS A TEST.
function produceStory(storyInfo){
		arr = storyInfo.split('^');
		var storyName = arr[0];
		var story = arr[1];

		$("#story-title").empty().append(storyName);

		$("#in0").empty().append($(userInput[0]));

		// append the story to the DOM
		$("#mad-story").empty().append(story);
		//show the story to the user
		$("#story").show();
		// empty the form's values
		$(':input').val('');
		// hide the questions
		$("#questions").hide();
}
function setStr(str){
	this.str = str;
}
function getStr(){
	return str;
}
