#!/usr/bin/node
const { argv } = require('node:process');
if (process.argv[2] === undefined)
{
	console.log('No argument');
}
else
{
	console.log(process.argv[2]);
}
