const request = require('request');

#!/usr/bin/node

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/films/${movieId}`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        const film = JSON.parse(body);
        const characters = film.characters;

        characters.forEach((characterUrl) => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else {
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});
