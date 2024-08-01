#!/usr/bin/node

const { error } = require('console');
const request = require('request');
const movieid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request.get(url, (error, response, body) => {
    if (error){
        console.log(error);
    }else{
        data = JSON.parse(body)
        console.log(data.title);
    }
})
