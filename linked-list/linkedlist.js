// Need an ordered list with fast inserts/removals at the beginning and end? use LL

// Lists 

// Do not have indexes!
// Connected via nodes with a next pointer
// Random access is not allowed

// Arrays
// Indexed in order!
// Insertion and deletion can be expensive
// Can quickly be accessed at a specific index


// insertAtBeginning
// addToHead - append
// insertAtEnd
// getAt - get data
// insertAt
// deleteFirstNode
// deleteLastNode
// deleteAt
// deleteList
// reverse
// indexOf
// isEmpty
// listSize
// getFirst
// getLast
// printList
// findNode - search
// deleteNode

class Node {
  constructor(data, next = null) {
    (this.data = data), // value
      (this.next = next); //reference to next node - next
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }
}

LinkedList.prototype.insertAtBeginning = function (data) {
  // A newNode object is created with property data and next = null
  let newNode = new Node(data);
  // The pointer next is assigned head pointer so that both pointers now point at the same node.
  newNode.next = this.head;
  // As we are inserting at the beginning the head pointer needs to now point at the newNode.

  this.head = newNode;
  return this.head;
};

// appendnode
LinkedList.prototype.addToHead = function (value) {
  // create a new node using our Node class from before
  const newNode = new Node(value);
  // edge case: linkedList is empty
  if (this.head === null) {
    // set the head of the linkedList to the new node
    this.head = newNode;
  } else {
    // find the current head node
    const currentHead = this.head;
    // reassign the head to our new node
    this.head = newNode;
    // set its next pointer to the current head
    newNode.next = currentHead;
  }
};

// addToTail
LinkedList.prototype.insertAtEnd = function (data) {
  // A newNode object is created with property data and next=null

  let newNode = new Node(data);
  // When head = null i.e. the list is empty, then head itself will point to the newNode.
  if (!this.head) {
    this.head = newNode;
    return this.head;
  }
  // Else, traverse the list to find the tail (the tail node will initially be pointing at null), and update the tail's next pointer.
  let tail = this.head;
  while (tail.next !== null) {
    tail = tail.next;
  }
  tail.next = newNode;
  return this.head;
};

// A helper function getAt() is defined to get to the desired position. This function can also be later used for performing delete operation from a given position.
LinkedList.prototype.getAt = function (index) {
  let counter = 0;
  let node = this.head;
  while (node) {
    if (counter === index) {
      return node;
    }
    counter++;
    node = node.next;
  }
  return null;
};
// The insertAt() function contains the steps to insert a node at a given index.
LinkedList.prototype.insertAt = function (data, index) {
  // if the list is empty i.e. head = null
  if (!this.head) {
    this.head = new Node(data);
    return;
  }
  // if new node needs to be inserted at the front of the list i.e. before the head.
  if (index === 0) {
    this.head = new Node(data, this.head);
    return;
  }
  // else, use getAt() to find the previous node.
  const previous = this.getAt(index - 1);
  let newNode = new Node(data);
  newNode.next = previous.next;
  previous.next = newNode;

  return this.head;
};

LinkedList.prototype.deleteFirstNode = function () {
  if (!this.head) {
    return;
  }
  this.head = this.head.next;
  return this.head;
};

LinkedList.prototype.deleteLastNode = function () {
  if (!this.head) {
    return null;
  }
  // if only one node in the list
  if (!this.head.next) {
    this.head = null;
    return;
  }
  let previous = this.head;
  let tail = this.head.next;

  while (tail.next !== null) {
    previous = tail;
    tail = tail.next;
  }

  previous.next = null;
  return this.head;
};

LinkedList.prototype.deleteAt = function (index) {
  // when list is empty i.e. head = null
  if (!this.head) {
    this.head = new Node(data);
    return;
  }
  // node needs to be deleted from the front of the list i.e. before the head.
  if (index === 0) {
    this.head = this.head.next;
    return;
  }
  // else, use getAt() to find the previous node.
  const previous = this.getAt(index - 1);

  if (!previous || !previous.next) {
    return;
  }

  previous.next = previous.next.next;
  return this.head;
};

LinkedList.prototype.deleteList = function () {
  this.head = null;
};

LinkedList.prototype.reverse = function () {
  let prevNode = null;
  let currentNode = this.head;
  if (currentNode === null) return;

  let nextNode;
  while (currentNode) {
    nextNode = currentNode.next;

    currentNode.next = prevNode;
    prevNode = currentNode;

    currentNode = nextNode;
  }
  this.head = prevNode;
};

// This function will return first index which matches with the passed element.
LinkedList.prototype.indexOf = function (data) {
  let ind = -1;
  let node = this.head;
  while (node) {
    ++ind;
    if (node.data === data) return ind;

    node = node.next;
  }
  return -1;
};

LinkedList.prototype.isEmpty = function () {
  return this.head == null;
};

LinkedList.prototype.listSize = function () {
  let size = 0;
  let node = this.head;
  while (node) {
    size++;
    node = node.next;
  }
  return size;
};
LinkedList.prototype.getFirst = function () {
  return this.head;
};
LinkedList.prototype.getLast = function () {
  let lastNode = this.head;
  if (lastNode) {
    while (lastNode.next) {
      lastNode = lastNode.next;
    }
  }
  return lastNode;
};
LinkedList.prototype.printList = function () {
  let node = this.head;
  console.log('HEAD->');
  while (node) {
    console.log(node.data + '->');
    node = node.next;
  }
  console.log('NULL');
};

LinkedList.prototype.findNode = function (value) {
  let current = this.head;
  while (current) {
    if (current.data === value) {
      return current;
    }
    current = current.next;
  }
  return null;
};

LinkedList.prototype.deleteNode = function (value) {
  if (this.head.value === value) {
    this.head = this.head.next;
  } else {
    let current = this.head;
    while (current.next) {
      if (current.next.value === value) {
        current.next = current.next.next;
        return;
      }
      current = current.next;
    }
  }
};

function print(x){
console.log(x);

}
let myList = new LinkedList();
print(myList.insertAtBeginning(2));

// HEAD->5->11->7->NULL

// node linked-list/linkedlist.js
