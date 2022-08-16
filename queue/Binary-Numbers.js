// Generate Binary Numbers from 1 to n
// Input: A positive integer n

// n = 3

// Output: Returns binary numbers in the form of strings from 1 up to n

// result = ["1","10","11"]

class Queue {

    constructor() {
        this.items = [];
        this.front = null;
        this.back = null;

    }



    isEmpty() {
        return this.items.length == 0;
    }

    getFront() {
        if (this.items.length != 0) {
            return this.items[0];
        } else
            return null;
    }

    size() {
        return this.items.length;
    }

    enqueue(element) {
        this.items.push(element);
    }



    dequeue() {
        if (this.items.length == 0) {
            return null;
        } else {
            return this.items.shift();


        }

    }


}

function findBin(n) {
    let result = [];
    let myQueue = new Queue();
    var s1, s2;
    myQueue.enqueue("1");
    for (var i = 0; i < n; i++) {

        result.push(myQueue.dequeue());
        s1 = result[i] + "0";
        s2 = result[i] + "1";

        myQueue.enqueue(s1);
        myQueue.enqueue(s2);

    }

    return result;
}

console.log(findBin(3))

// node queue/Binary-Numbers.js
