

$(document).ready(function(){
  console.log("Calling Server for Story List")
  $.ajax({
    url:'/get/story-list',
    type: 'get',
    success: function(data) {
      console.log("Successful Call")
      console.log(data);
      produceStoryList(data);
    },
    failure: function(data) {
      alert('Got an error dude');
    }
  });
  $("#StoryList").on('click', 'a', function(){
    id = this.id;
    console.log(id);
    console.log(id.split('y'));

    //alert(id);
    $.ajax({
      url:'/set/',
      type: 'post',
      data:{
        'id': id.split('y')[1]
      },
      success: function(data) {
        console.log("Successful Call");
        console.log(data);
        produceStoryList(data);
      },
      failure: function(data) {
        alert('Got an error dude');
      }
    });
  });
});


function produceStoryList(storyList){
  storyList = JSON.parse(storyList);
  for(var i=0; i<storyList.length; i++){
    story = storyList[i];
    $("#StoryList").append("<a class='storyClass'id='story"+i+"' href='/story'><b>" + story.fields.story_name + "</b></a><br>");
  }
}
