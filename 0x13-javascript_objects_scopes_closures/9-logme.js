#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
	consle.log(`${count++}: ${item}`);
};
