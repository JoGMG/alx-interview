#!/usr/bin/node
/*
A script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie
  ID - example: `3` = "Return of the Jedi".
- Display one character name per line in the same order
  as the "characters" list in the `/films/` endpoint.
- You must use the `Star wars API`: https://swapi-api.alx-tools.com/
- You must use the `request` module.
*/
const request = require('request');
const arg = process.argv[2];

function fetchCharacterName(url) {
    return new Promise((resolve, reject) => {
        request(url, { json: true }, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                resolve(body.name);
            }
        });
    });
}

if (process.argv.length !== 3) {
    console.log("Usage: node <file_name> <number>");
} else {
    request(`https://swapi-api.alx-tools.com/api/films/${arg}`, {json: true}, (error, response, body) => {
        if (error) {
            return console.log(error);
        }
    
        const characters = body.characters;
        const promises = characters.map(fetchCharacterName)
    
        Promise.all(promises)
            .then(names => names.forEach(name => console.log(name)))
            .catch(error => console.log(error));
    });
}
