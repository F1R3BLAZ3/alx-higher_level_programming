#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.results;

    if (Array.isArray(films)) {
      // Filter films that contain character ID 18 (Wedge Antilles)
      const wedgeAntillesFilms = films.filter((film) => {
        return film.characters.some((characterUrl) => {
          // Extract the character ID from the character URL
          const characterIdFromUrl = characterUrl.match(/(\d+)\/$/)[1];
          return characterIdFromUrl === characterId.toString();
        });
      });

      console.log(wedgeAntillesFilms.length);
    } else {
      console.error('Failed to retrieve film data.');
    }
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
