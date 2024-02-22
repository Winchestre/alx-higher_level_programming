#!/usr/bin/node
// A script that prints the number of movies where the character "Wedge Antilles"
// is present.

const request = require('request');
let count = 0;

request.get(process.argv[2], (error, response, body) => {
	if (error) {
		console.log(error);
	} else {
		const content = JSON.parse(body);
		content.results.map(film => {
			film.characters.map(character => {
				if (character.includes(18)) {
					count++;
				}
			});
		});
		console.log(count);
	}
});
