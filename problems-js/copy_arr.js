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