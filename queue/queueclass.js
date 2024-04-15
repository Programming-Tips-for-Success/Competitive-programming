// LL implementation

class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Queue {
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    enqueue(val){
        var newNode = new Node(val);
        if(!this.first){
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        return ++this.size;
    }

    dequeue(){
        if(!this.first) return null;

        var temp = this.first;
        if(this.first === this.last) {
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.value;
    }
}
function print(x){
console.log(x);

}
// Insertion -   O(1)

// Removal -   O(1)

// Searching -   O(N)

// Access -   O(N)

var queue = new Queue();
print(queue.enqueue(10)) // 1
queue.size // 1
queue.enqueue(100) // 2
queue.size // 2
queue.enqueue(1000) // 3
queue.size // 3

// node queue/queueclass.js
