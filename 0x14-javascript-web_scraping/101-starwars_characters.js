#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (error, reponse, body) {
  if (error) {
    console.error(error);
  }
  const filmdatas = JSON.parse(body);
  request(filmdatas, function (error, reponse, body) {
    if (error) {
      console.error(error);
    }
    const filmcharacter = JSON.parse(body);
    const endpoints = filmcharacter.characters;
    endpoints.forEach((endpoint) => {
      request(endpoint, function (error, reponse, body) {
        if (error) {
          console.error(error);
        }
        const characterdata = JSON.parse(body);
        console.log(characterdata.name);
      });
    });
  });
});
