

// let queue1 = [];
// queue1.push(1);          // [1]
// queue1.push(2);          // [1, 2]
// let first = queue1.shift();//[2]
// console.log(first, queue1);     // 1

// program to implement queue data structure

// class Queue {
//     constructor() {
//         this.items = [];
//     }
    
//     // add element to the queue
//     enqueue(element) {
//         return this.items.push(element);
//     }
    
//     // remove element from the queue
//     dequeue() {
//         if(this.items.length > 0) {
//             return this.items.shift();
//         }
//     }
    
//     // view the last element
//     peek() {
//         return this.items[this.items.length - 1];
//     }
    
//     // check if the queue is empty
//     isEmpty(){
//        return this.items.length == 0;
//     }
   
//     // the size of the queue
//     size(){
//         return this.items.length;
//     }
 
//     // empty the queue
//     clear(){
//         this.items = [];
//     }
// }

// let queue = new Queue();
// queue.enqueue(1);
// queue.enqueue(2);
// queue.enqueue(4);
// queue.enqueue(8);
// console.log(queue.items);

// queue.dequeue();
// console.log(queue.items);

// console.log(queue.peek());

// console.log(queue.isEmpty());

// console.log(queue.size());

// queue.clear();
// console.log(queue.items);

class CircularQueue {
    constructor(size) {
     this.element = [];
     this.size = size
     this.length = 0
     this.front = 0
     this.back = -1
    }
   isEmpty() {
     return (this.length == 0)
    }
   enqueue(element) {
     if (this.length >= this.size) throw (new Error("Maximum length exceeded"))
     this.back++
      this.element[this.back % this.size] = element
     this.length++
    }
   dequeue() {
     if (this.isEmpty()) throw (new Error("No elements in the queue"))
     const value = this.getFront()
     this.element[this.front % this.size] = null
     this.front++
     this.length--
     return value
    }
   getFront() {
     if (this.isEmpty()) throw (new Error("No elements in the queue"))
     return this.element[this.front % this.size]
    }
   clear() {
     this.element = new Array()
     this.length = 0
     this.back = -1
     this.front = 0
    }
   }

let queue2 = new CircularQueue(5);
queue2.enqueue(1);
queue2.enqueue(2);
queue2.enqueue(4);
queue2.enqueue(8);
console.log(queue2.element);
queue2.dequeue();
console.log(queue2.element);

// node queue/queue.js