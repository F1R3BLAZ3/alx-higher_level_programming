$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Display the translation of "hello" in the <div> with id "hello"
    $('#hello').text(data.hello);
  });
});
