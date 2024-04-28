'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function () {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'getImmutableCopy' and 'isMutable' function below.
 */

class MyClass {
    constructor(a, b, c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    sum() {
        return this.a + this.b + this.c;
    }

    /*
     * The function 'getImmutableCopy' is expected to return a copy of instance which doesn't allow the member variables to be overwritten.
    */
    getImmutableCopy() {

    }

    /*
    * The function 'isMutable' is expected to return a boolean which denotes whether the instance is mutable or not.
    */
    isMutable() {

    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let in_arr = readLine().split(' ');

    let a = parseInt(in_arr[0]);
    let b = parseInt(in_arr[1]);
    let c = parseInt(in_arr[2]);

    let obj = new MyClass(a, b, c);
    let immutableObj = obj.getImmutableCopy();
    try {
        immutableObj.a = -1;
        immutableObj.b = -1;
        immutableObj.c = -1;
    }
    catch (err) { }

    if (obj.a === a && obj.b === b && obj.c === c && obj.a === immutableObj.a && obj.b === immutableObj.b && obj.c === immutableObj.c && (immutableObj instanceof MyClass)) {
        ws.write('true\n');
    }
    else {
        ws.write('false\n');
    }
    ws.write(obj.isMutable() + '\n');
    ws.write(immutableObj.isMutable() + '\n');

    ws.end();
}



// 3. JavaScript: Immutable Copy
// A class called MyClass is implemented in the provided code. It contains 3 member variables a,b, and c, and a member method called sum().

 

// Implement two member methods for MyClass:

// getImmutableCopy() - returns a copy of the class instance that does not allow any of the class variables a, b, or c to be overwritten
// isMutable() - returns a boolean on whether the class is mutable
 
// For example, an instance of MyClass named obj is created with values a = 3, b = 4, c = 5. When an attempt to assign a value of 1 to variable a using the getImmutableCopy() method as obj.getImmutableCopy().a = 1, the value of a should not change. A call to obj.isMutable() returns true, whereas obj.getImmutableCopy().isMutable() should return false.

 

// Constraints

// 1 ≤ a,b,c ≤ 1000
 

// Input Format For Custom Testing
// The first and only line contains 3 space-separated integers a,b, and c.

// Sample Case 0
// Sample Input For Custom Testing

// 3 4 5
// Sample Output

// true
// true
// false
// Explanation



// The first line shows the output of whether the immutable copy is immutable or not.

// The second line shows the output obtained from the isMutable method called on the object.

// The third line shows the output obtained from the isMutable method called on the immutable copy of the object.

// Sample Case 1
// Sample Input For Custom Testing

// 1 2 3
// Sample Output

// true
// true
// false



// var Food = {
//   cuisine: 'abc',
// };
// var food1 = Object.create(Food);
// delete food1.cuisine;
// console.log(food1.cuisine, Food, food1); // abc { cuisine: 'abc' } {}

// //  copy object problem-
// let obj = {
//   a: 1,
//   b: 2,
//   c: {
//     age: 30,
//   },
// };
// // var objclone = Object.assign({},obj); // instead of this we can use spread operator
// var objclone = { ...obj };

// console.log('objclone: ', objclone); // { a: 1, b: 2, c: { age: 30 } }
// obj.c.age = 45;
// console.log('After Change - obj: ', obj); // 45 - This also changes  { a: 1, b: 2, c: { age: 45 } }
// console.log('After Change - objclone: ', objclone); // 45  { a: 1, b: 2, c: { age: 45 } }

// // solution ?

// // value update ?
// var a = {},
//   b = { key: 'b' },
//   c = { key: 'c' };
// a[b] = 123;
// a[c] = 456;
// console.log(a[b], a[c]); // 456 456

// var checkProp = { hasownProperty: 1, foo: 2 };

// console.log(checkProp.hasOwnProperty('foo'), 'hasOwnProperty'); // true

// let obj3 = { person: 'John', age: 21 };
// Object.freeze(obj3);

// var det = { name: 'Tom', ID: 'E1001' };
// var copy = Object.assign({}, det);

// var o1 = { a: 10 };
// var o2 = { b: 20 };
// var o3 = { c: 30 };
// var obj2 = Object.assign(o1, o2, o3);
// console.log(obj2); // {a: 10, b: 20, c: 30}
// console.log(o1); // {a: 10, b: 20, c: 30}
// var o1 = { a: 10 };
// var obj4 = Object.assign(o1);
// obj4.a++;
// console.log("Value of 'a' in the Merged object after increment  ");
// console.log(obj4.a);
// console.log(o1.a);
// console.log("value of 'a' in the Original Object after increment ");

// let demoObj = { name: 'smith', age: 24 };
// console.log(Object.keys(demoObj)); // ["name", "age"]

// let demoObj2 = { name: 'smith', age: 24 };
// console.log(Object.values(demoObj2)); // ["smith", 24]

// const item = {
//   isAvailable: false,
//   itemDescription: function () {
//     console.log(`${this.name} ${this.isAvailable}`);
//   },
// };
// console.log(item); // {isAvailable: false, itemDescription: ƒ}
// const me = Object.create(item);
// me.name = 'cheese'; // "name" is a property set on "me", but not on "person"
// me.isAvailable = true; // inherited properties can be overwritten
// me.itemDescription();
// console.log(me); // {name: "cheese", isAvailable: true}