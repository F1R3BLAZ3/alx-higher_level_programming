$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the JSON response
    const characterName = data.name;

    // Display the character name in the <div> with id "character"
    $('#character').text(characterName);
  });
});
