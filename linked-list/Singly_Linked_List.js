// Linked lists tend not to do very well with accessing and sorting numbers. 

// piece of data - val
//reference to next node - next

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  //     This function should accept a value
  // Create a new node using the value passed to the function
  // If there is no head property on the list, set the head and tail to be the newly created node
  // Otherwise set the next property on the tail to be the new node and set the tail property on the list to be the newly created node
  // Increment the length by one
  // Return the linked list
  push(val) {
    var newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }
  // If there are no nodes in the list, return undefined
  // Loop through the list until you reach the tail
  // Set the next property of the 2nd to last node to be null
  // Set the tail to be the 2nd to last node
  // Decrement the length of the list by 1
  // Return the value of the node removed
  pop() {
    if (!this.head) return undefined;
    var current = this.head;
    var newTail = current;
    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    this.tail.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }

  shift() {
    if (!this.head) return undefined;
    var currentHead = this.head;
    this.head = currentHead.next;
    this.length--;
    if (this.length === 0) {
      this.tail = null;
    }
    return currentHead;
  }

  unshift(val) {
    var newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }

// TODO update tail value also
 rotate(k) {
        if (k == 0)
            return;
  
        // Let us understand the 
        // below code for example k = 4
        // and list = 10->20->30->40->50->60.
        var current = this.head;
  
        // current will either point to kth 
        // or NULL after this
        // loop. current will point to node 
        // 40 in the above example
        var count = 1;
        while (count < k && current != null) {
            current = current.next;
            count++;
        }
  
        // If current is NULL, k is greater
        // than or equal to count
        // of nodes in linked list. 
        // Don't change the list in this case
        if (current == null)
            return;
  
        // current points to kth node. 
        // Store it in a variable.
        // kthNode points to node 40 
        // in the above example
        var kthNode = current;
  
        // current will point to last
        // node after this loop
        // current will point to node 
        // 60 in the above example
        while (current.next != null)
            current = current.next;
  
        // Change next of last node to previous head
        // Next of 60 is now changed to node 10
  
        current.next = this.head;
  
        // Change head to (k+1)th node
        // head is now changed to node 50
        this.head = kthNode.next;
  
        // change next of kth node to null
        kthNode.next = null;
    }

  get(index) {
    if (index < 0 || index >= this.length) return null;
    var counter = 0;
    var current = this.head;
    while (counter !== index) {
      current = current.next;
      counter++;
    }
    return current;
  }

  set(index, val) {
    var foundNode = this.get(index);
    if (foundNode) {
      foundNode.val = val;
      return true;
    }
    return false;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) return false;
    if (index === this.length) return !!this.push(val);
    if (index === 0) return !!this.unshift(val);

    var newNode = new Node(val);
    var prev = this.get(index - 1);
    var temp = prev.next;
    prev.next = newNode;
    newNode.next = temp;
    this.length++;
    return true;
  }

  remove(index) {
    if (index < 0 || index >= this.length) return undefined;
    if (index === 0) return this.shift();
    if (index === this.length - 1) return this.pop();
    var previousNode = this.get(index - 1);
    var removed = previousNode.next;
    previousNode.next = removed.next;
    this.length--;
    return removed;
  }

  reverse() {
    var node = this.head;
    this.head = this.tail;
    this.tail = node;
    var next;
    var prev = null;
    for (var i = 0; i < this.length; i++) {
      next = node.next;
      node.next = prev;
      prev = node;
      node = next;
    }
    return this;
  }
  print() {
    var arr = [];
    var current = this.head;
    while (current) {
      arr.push(current.val);
      current = current.next;
    }
    console.log(arr);
  }
}

function showLog(x){
console.log(x);

}

// Insertion -   O(1)

// Removal -   It depends.... O(1) or O(N)

// Searching -   O(N)

// Access -   O(N)

// var first = new Node('Hi');
// first.next = new Node('there');
// first.next.next = new Node('how');
// first.next.next.next = new Node('are');
// first.next.next.next.next = new Node('you');

var list = new SinglyLinkedList();
// list.push('HELLO');
// list.push('GOODBYE');
// print(list);


// list.push(5); // list
// showLog(list.length); // 1
// showLog(list.head.val); // 5
// showLog(list.tail.val); // 5
 
// list.push(10); // list
// showLog(list.length); // 2
// showLog(list.head.val); // 5
// showLog(list.head.next.val); // 10
// showLog(list.tail.val); // 10
 
// list.push(15); // list
// list.length; // 3
// list.head.val; // 5
// list.head.next.val; // 10
// list.head.next.next.val; // 15
// list.tail.val; // 15
 
// showLog(list.pop().val); // 15
// showLog(list.tail.val); // 10
// showLog(list.length); // 2
// showLog(list.pop().val); // 10
// showLog(list.length); // 1
// showLog(list.pop().val); // 5
// showLog(list.length); // 0
// showLog(list.pop()); // undefined
// showLog(list.length); // 0


// list.push(5).push(10).push(15).push(20);  // list
// showLog(list.get(0).val) // 5
// showLog(list.get(1).val) // 10
// list.get(2).val // 15
// list.get(3).val // 20
// list.get(4) // null

// list.insert(2,12); // true
// list.insert(100,12); // false
// list.length // 5
// list.head.val // 5
// list.head.next.val // 10
// list.head.next.next.val // 12
// list.head.next.next.next.val // 15
// list.head.next.next.next.next.val // 20
 
// list.insert(5,25); // true
// list.head.next.next.next.next.next.val //25
// list.tail.val // 25

// showLog(list.set(0,10)) // true
// list.set(1,2) // true
// list.length // 2
// list.head.val // 10
 
// showLog(list.set(10,10)) // false
 
// list.set(3,100) // true
// list.head.next.next.next.val; // 10


// list.push(5).push(10).push(15).push(20).push(25);  // list
// showLog(list.head.val); // 5
// showLog(list.tail.val); // 25;
 
// list.rotate(3);
// showLog(list.head.val); // 20
// showLog(list.head.next.val); // 25
// showLog(list.head.next.next.val); // 5
// showLog(list.head.next.next.next.val); // 10
// showLog(list.head.next.next.next.next.val); // 15
// showLog(list.tail.val); // 15
// showLog(list.tail.next); // null

// list.push(5).push(10).push(15).push(20).push(25);  // list
// list.head.val; // 5
// list.tail.val; // 25;
 
// list.rotate(-1);
// list.head.val; // 25
// list.head.next.val; // 5
// list.head.next.next.val; // 10
// list.head.next.next.next.val; // 15
// list.head.next.next.next.next.val; // 20
// list.tail.val; // 20
// list.tail.next // null


// list.push(5).push(10).push(15).push(20).push(25);  // list
// list.head.val; // 5
// list.tail.val; // 25;
 
// list.rotate(1000);
// list.head.val; // 5
// list.head.next.val; // 10
// list.head.next.next.val; // 15
// list.head.next.next.next.val; // 20
// list.head.next.next.next.next.val; // 25
// list.tail.val; // 25
// list.tail.next // null

list.push(5).push(10).push(15).push(20);
list.remove(2).val; // 15
list.remove(100); // undefined
list.length // 3
list.head.val // 5
list.head.next.val // 10
list.head.next.next.val // 20

// node linked-list/Singly_Linked_List.js
