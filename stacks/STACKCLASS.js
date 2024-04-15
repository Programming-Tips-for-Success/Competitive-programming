// LINKED LIST IMPLEMENTATION

class Stack {
    constructor(){
        this.first = null;
        this.last = null;
        this.size = 0;
    }

        push(val){
        var newNode = new Node(val);
        if(!this.first){
            this.first = newNode;
            this.last = newNode;
        } else {
            var temp = this.first;
            this.first = newNode;
            this.first.next = temp;
        }
        return ++this.size;
    }
    pop(){
        if(!this.first) return null;
        var temp = this.first;
        if(this.first === this.last){
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.value;
    }
}

class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }

 
}

function print(x){
console.log(x);

}

var stack = new Stack();
 
// print(stack.push(10)) // 1
// print(stack.first.value) // 10
// print(stack.last.value) // 10
// stack.push(100);
// stack.first.value // 100
// stack.last.value // 10
// stack.push(1000);
// stack.first.value // 1000
// stack.last.value // 10
 
// stack.push(10) // 1
// stack.size // 1
// stack.push(100) // 2
// stack.size // 2
// stack.push(1000) // 3
// stack.size // 3

// stack.push(10);
// stack.push(100);
// stack.push(1000);
// var removed = stack.pop();
// print(removed) // 1000
// print(stack.size) // 2
// stack.pop();
// stack.pop();
// stack.size // 0

stack.push(10).push(20).push(30)
print(stack.pop()) // 30
stack.pop() // 20
stack.pop() // 10
print(stack.pop()) // null
stack.push(30).push(40).push(50)
stack.pop() // 50
stack.push(60)
stack.pop() // 60

// Insertion -   O(1)

// Removal -   O(1)

// Searching -   O(N)

// Access -   O(N)

// node stacks/STACKCLASS.js