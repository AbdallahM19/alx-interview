#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const promises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  Promise.all(promises)
    .then(names => {
      names.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
