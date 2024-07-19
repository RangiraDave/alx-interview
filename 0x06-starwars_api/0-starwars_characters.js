#!/usr/bin/node

const request = require('request');

/**
 * Sends a request to retrieve and display the names of characters from a Star Wars movie.
 * @param {string[]} characterList - The list of character URLs.
 * @param {number} index - The index of the current character in the list.
 * @returns {void}
 */
function sendRequest(characterList, index) {
    if (characterList.length === index) {
        return;
    }

    request(characterList[index], (error, response, body) => {
        if (error) {
            console.log(error);
        } else {
            console.log(JSON.parse(body).name);
            sendRequest(characterList, index + 1);
        }
    });
}

/**
 * Retrieves the character list for a given Star Wars movie and calls the sendRequest function.
 * @param {string} movieId - The ID of the Star Wars movie.
 * @returns {void}
 */
const movieEndpoint = 'https://swapi-api.hbtn.io/api/films/1/';
request(movieEndpoint, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const characterList = JSON.parse(body).characters;

        sendRequest(characterList, 0);
    }
});
