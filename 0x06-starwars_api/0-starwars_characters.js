#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (movieId && process.argv.length > 2) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
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
}
