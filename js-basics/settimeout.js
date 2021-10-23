// What is logged? 

// it logs 5 five times since settimeout runs the log function after for loop is done.
// settimeout is an async process.

let i;
for (i = 0; i < 5; i++) {
const log = () => {
  console.log(i); // 5  5 times
}
setTimeout(log, 100);
}

for (var g = 0; g < 5; g++) {
  setTimeout(function () {
  console.log(g, 'g');
  },100);
  }
  
  // 5
  // 5
  // 5
  // 5
  // 5
// we can resolve this problem by passing i in the log method.

let j;
for (j = 0; j < 5; j++) {
const log = (i) => {
  console.log(j);
}
setTimeout(log, 100, j);
}

// example
console.log('one');
setTimeout(function() {  // this function will run in end after promise
  console.log('two');
}, 0);
Promise.resolve().then(function() {
  console.log('three');
})
console.log('four');

// one
// four
// three
// two

// example
var obj = {
	id: "awesome",
	cool: function coolFn() {
		console.log( this.id );
	}
};

var id = "not awesome";

obj.cool(); // awesome

// problem
setTimeout( obj.cool, 100 ); // undefined

// solution?

// const arr = [10, 12, 15, 21];
// for (var k = 0; k < arr.length; k++) {
//   setTimeout(function() {
//     console.log('Index: ' + k + ', element: ' + arr[k]);
//   }, 1000);
// } // log 4 five times

// Closures can be used to prevent this problem by creating a unique scope for each iteration,
// storing each unique value of the variable within its scope, as follows:

// const arr = [10, 12, 15, 21];
// for (var l = 0; l < arr.length; l++) {
//   // pass in the variable i so that each function 
//   // has access to the correct index
//   setTimeout(function(i_local) {
//     return function() {
//       console.log('The index of this number is: ' + i_local);
//     }
//   }(l), 1000);
// } // log 0, 1, 2, 3


// Another way to solve the above issue is by using let keyword

const arr = [10, 12, 15, 21];
for (let a = 0; a < arr.length; a++) {
  setTimeout(function() {
    console.log('The index of this number is: ' + a);
  }, 3000);
}



// Write a function that will loop through a list of integers and print the index of each element after a 3-second delay.

for (var b = 0; b < 3; b++) {
  setTimeout(function(il) { 
return function() {
  console.log(il);
}  
    }(b), 1000 + b);
}

for (var c = 0; c < 5; c++) {
             setTimeout(function() { console.log(c, 'c'); }, c * 1000 );
}

for (var d = 0; d < 5; d++) {
  (function(d){
   setTimeout(function() { console.log(d, 'd'); }, d * 1000 );
  }(i))
          
}

for(var e = 0; e < 10; e++) {
  setTimeout(console.log.bind(console, e, 'e'), 10);
}

for (var f = 0; f < 3; f++) { setTimeout(function log() { console.log(f, 'f'); 
}, 1000); }

// example
function doAsyncTask(cb) {

  setTimeout(() => {

    console.log("Async Task Calling Callback");

    cb();

  },

    1000);

}

doAsyncTask(() => console.log("Callback Called"));

// example
setTimeout(function cb1() {
  console.log('cb1');
}, 5000); 


let p1 = new Promise((resolve, reject) => {
  resolve("foo");
  });
  let p2 = new Promise((resolve, reject) => {
  reject("bar");
  });
  console.log("bip");
  p1.then(val => {
  console.log(val);
  return p2;
  })
  .then(val => {
  console.log("baz");
  })
  .catch(err => {
  console.log(err);
  });
  console.log("bop");
  
  // bip
  // bop
  // foo
  // bar

  
// node js-basics/settimeout.js