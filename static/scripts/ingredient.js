
$(document).ready(function () {
  $('.searchbutton').on('click', function () {  
    window.location.assign("/search/" + this.id);
    });
})