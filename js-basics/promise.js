
// create function sum with promises if the values are string then reject otherwise resolve it

// function sumValidate(a, b) {

//     let a = new Promise((resolve, reject)=>{
//      if(typeof a='string' || typeof b='string')
//     reject('err')
//     sum  = a +b
//     resolve(sum),
    
//     })
//     }
    
//     async function finalSum(){
//     try {
//     final = await sumValidate(2, 4)
//     return final;
//     } catch (err){
//     console.log(err)
//     }
    
//     }
//     final = sumValidate(2, 4).then((output)=>{
//     return output;
//     }, catch(err)=>
//     console.log(err)
//     )
    

doit().then(function () { log('Now finally done!') });
   log('---- But notice where this ends up!');

   function doit() {
     return new Promise(async function (resolve, reject) {
       log('Calling someTimeConsumingThing');
       await someTimeConsumingThing();
       log('Ready with someTimeConsumingThing');
       resolve();
     })
   }

   function someTimeConsumingThing() {
     return new Promise(function (resolve, reject) {
       setTimeout(resolve, 2000);
     })
   }

   function log(txt) {
     setTimeout(() => {
    //    (<HTMLDivElement>document.getElementById('msg')).innerHTML += txt + '<br>'
     }, 1000);
   }

{/* Example2- */}

const CONDITION = true;
   // Data passed when the promise is resolved
   const DATA = 'hello world';
   // Error passed when the promise is rejected
   const ERROR = new Error('Ooops!');
   const promise =
     new Promise((resolve, reject) => {
       // do some async stuff
       if (CONDITION) resolve(DATA);
       else reject(ERROR);
     })
       .then(
         (data) => { console.log(data); },
         (err) => { console.log(err); }
       );

// Example3-

  let firstPromise = Promise.resolve(10);
   let secondPromise = Promise.resolve(5);
   let thirdPromise = Promise.resolve(20);
   Promise.all([firstPromise, secondPromise, thirdPromise])
     .then(values => {
       console.log(values, 'v');
     });

// Example4-
//  You can use the Promise.race(iterable) function when you want the value of the first promise that resolves or rejects.

  let promise1 = new Promise((resolve, reject) => {
     setTimeout(resolve, 2000, 'promise 1 resolved');
   });

   let promise2 = new Promise((resolve, reject) => {
     setTimeout(reject, 3000, 'promise 2 rejected');
   });
   Promise
     .race([promise1, promise2])
     .then(console.log)
     .catch(console.log);

// Example5-

  function Person(options) {
     return new Promise((resolve, reject) => {
       if (typeof options.age === 'number') { // typeof is used to check that this property is present or not.
         if (options.age < 18) {
           reject(new Error('You are not of legal age.'))
         }
         resolve(`${options.name} you are authorized for accessing our content.`)
       }
       reject('Request rejected.')
     })
   }
   Person({ age: '15', name: 'sam' }).then(res => {
     console.log(res, 'res');
   }).catch(error => {
     console.error(error);
   });

   (async function () {
     let result = await Person({ name: "John", age: 22 })
       .catch(err => console.log(err))
     if (result !== undefined) {
       console.log(result)
     } else {
       console.log('process not fullfilled')
     }
   }())

// Example6-

function getSum(n1, n2) {
     var isAnyNegative = function () {
       return n1 < 0 || n2 < 0;
     }
     var promise = new Promise(function (resolve, reject) {
       if (isAnyNegative()) {
         reject(Error("Negatives not supported"));
       }
       resolve(n1 + n2)
     });
     return promise;
   }

   getSum(5, -3)
     .then(function (result) {
       console.log(result);
     },
       function (error) {
         console.log(error.message);
       });
   //nw23
   function getSum2(n1, n2) {
     var isAnyNegative = function () {
       return n1 < 0 || n2 < 0;
     }
     var promise = new Promise(function (resolve, reject) {
       if (isAnyNegative()) {
         reject(Error("Negatives not supported"));
       }
       resolve(n1 + n2);
     });
     return promise;
   }

   getSum2(5, 6)
     .then(function (result) {
       console.log(result);
       return getSum(10, 20);
       //this returns another Promise    
     },
       function (error) {
         console.log(error);
       })
     .then(function (result) {
       console.log(result);
       return getSum(30, 40);
       //this returns another Promise    
     },
       function (error) {
         console.log(error);
       })
     .then(function (result) {
       console.log(result);
     },
       function (error) {
         console.log(error);
       });

   console.log("End of script ");

// Example7-

function delay(time) {
     return new Promise(function (resolve, reject) {
       setTimeout(resolve, time);
     });
   }

   delay(1000)
     .then(function () {
       console.log("after 1000ms");
       return delay(2000);
     })
     .then(function () {
       console.log("after another 2000ms");
     })
     .then(function () {
       console.log("step 4 (next Job)");
       return delay(5000);
     })

// Example8-

 function getNumber1() {
     return Promise.resolve('374');
   }
   // This function does the same as getNumber1
   async function getNumber2() {
     return 374;
   }

   function f1() {
     return Promise.reject('Some error');
   }
   async function f2() {
     throw 'Some error';
   }

// Example9-


     function doSomething() {
         console.log("I promise to return at some point.");
         return new Promise(function (resolve, reject) {
           const  allIsGood = someLongRunningActivity();
             if (allIsGood) {
                 console.log("Resolving the promise.");
                 resolve();
             } else {
                 console.log("Something bad happened, don't forget to check for errors!");
                 reject();
             }
         });
     }

     
    function  someLongRunningActivity() {
       //run a query or perform some calculation
       return true;
   }

doSomething()
     .then(() => {
       console.log("The promise was honored, you can do what you were waiting to do.");
     })
     .catch(() => {
       console.log("You remembered to check for errors!");
     });

 
const p1 = new Promise((resolve, reject) => {
    console.log("Promise has started");
    const lifeIsEasy = false;
    if (lifeIsEasy) {
        //Value to be returned if the promise is resolved
        //return value is optional
        resolve("No it's not");
    }
    else {
        //Value to be returned if the promise is rejected
        //return value is also optional
        reject("welcome to the real world");
    }
});
//then is executed when the promise is resolved
p1.then(value => {
    console.log(value);
})
//catch is executed when the promise is rejected
  .catch (err => {
    console.log(err);
});
 
/*expected output
Promise has started
welcome to the real world*/

 



    
    
    
    
    