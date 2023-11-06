$(document).ready(function () {
  // Wait for the DOM to be fully loaded
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the movie titles from the JSON response
    const movies = data.results;

    // Select the <ul> element with id "list_movies"
    const listMovies = $('#list_movies');

    // Loop through the movie titles and add them to the list
    $.each(movies, function (index, movie) {
      const title = movie.title;
      const listItem = $('<li>').text(title);
      listMovies.append(listItem);
    });
  });
});
