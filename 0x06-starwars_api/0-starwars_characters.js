#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the movie API
const url = `https://swapi-api.alx-tools.com/films/${movieId}`;

// Make a request to the movie API
request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        // Parse the response body into a JSON object
        const film = JSON.parse(body);
        const characters = film.characters;

        // Iterate over each character URL
        characters.forEach((characterUrl) => {
            // Make a request to the character API
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else {
                    // Parse the response body into a JSON object
                    const character = JSON.parse(body);
                    console.log(character.name);
                }
            });
        });
    }
});
