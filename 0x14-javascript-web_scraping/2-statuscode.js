#!/usr/bin/node

const fs = require('fs');
const url = process.argv[2];

fs.get(url, (error, response) => {
    if (error){
        console.log(error);
    }
    else{
        console.log(`code:${response.statusCode}`)
    }
})
