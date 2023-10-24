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
      const wedgeAntillesFilms = films.filter((film) => film.characters.includes(characterId));

      console.log(wedgeAntillesFilms.length);
    } else {
      console.error('Failed to retrieve film data.');
    }
  } else {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
