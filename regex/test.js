let str2 = "The rain in Spain stays mainly in the plain";
// Here we simply matching ain with whole string.
let patt1 = /ain/g;
console.log(str2.match(patt1)) //[ 'ain', 'ain', 'ain', 'ain' ]

// pass variables in regex-
console.log(("str1,str2,str3,str4".match(/str/g) || []).length); //logs 4
console.log(("str1,str2,str3,str4".match(new RegExp("str", "g")) || []).length); //logs 4

var str = "Give 100%!";
var pattern = /\d/g;
console.log(str.match(pattern));// ["1", "0", "0"]

console.log(pattern.test(str)); // true

var str = "Give 100%!";
var pattern = /\D/g;
console.log(str.match(pattern));// ["G", "i", "v", "e", " ", "%", "!"]

var str = "Hello 100%!";
var pattern = /\w/g;
console.log(str.match(pattern)); // ["H", "e", "l", "l", "o", "1", "0", "0"]

var str = "Hello 100%!";
var pattern = /\W/g;
console.log(str.match(pattern));// [" ", "%", "!"]

var str = "app. component. html";
var pattern = /\s/g;
console.log(str.match(pattern));// [" ", " "]

var str = "app comp";
var pattern = /\S/g;
console.log(str.match(pattern)); // ["a", "p", "p", "c", "o", "m", "p"]

let quote = "eat code sleep repeat eat.. ";
var regex = /eat/g;
var match4 = quote.match(regex);
console.log(match4)  // ["eat", "eat", "eat"]

let quote2 = "eat code sleep repeat eat.. ";
var regex = /eat/m;
var match4 = quote2.match(regex);
console.log(match4)//  ["eat"]

var str = "coders schools";
var pattern = /Schools/i;
console.log(str.match(pattern)); // ["schools"]


let newRe = new RegExp('Fox') // new RegExp(/Fox/);
let str3 = 'The Quick BrownFox Jumps Over The Lazy Dog ';
console.log(newRe.test(str3)) // true

console.log(/(hey|ho)/.exec('hey'))  // [ 'hey', 'hey', index: 0, input: 'hey', groups: undefined ]

// regex to replace any text –
console.log("Hello world!".replace(/world/, 'dog'))  // Hello dog!





