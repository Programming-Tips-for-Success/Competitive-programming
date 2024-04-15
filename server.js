let http = require('http');
let fs = require('fs');
// const jknk = './index.html';
// const jknk1 = './graph/graph-q.html';
const jknk = './tree/sum_prob.html';


let handleRequest = (request, response) => {
    response.writeHead(200, {
        'Content-Type': 'text/html'
    });
    fs.readFile(jknk, null, function (error, data) {
        if (error) {
            response.writeHead(404);
            respone.write('Whoops! File not found!');
        } else {
            response.write(data);
        }
        response.end();
    });
};

http.createServer(handleRequest).listen(8000); 
 
//  node server.js
 
 
 
 
 
 
 
 
