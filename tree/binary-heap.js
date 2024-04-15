// Need to write a scheduler?
// Use a binary heap!

// Very similar to a binary search tree, but with some different rules!

// In a MaxBinaryHeap, parent nodes are always larger than child nodes. In a MinBinaryHeap, parent nodes are always smaller than child nodes


// MAX BINARY HEAP
// Each parent has at most two child nodes
// The value of each parent node is always greater than its child nodes
// In a max Binary Heap the parent is greater than the children, but there are no guarantees between sibling nodes.
// A binary heap is as compact as possible. All the children of each node are as full as they can be and left children are filled out first

// Binary Heaps are used to implement Priority Queues, which are very commonly used data structures
// They are also used quite a bit, with graph traversal Algorithms

class MaxBinaryHeap {
    constructor(){
        this.values = [];
    }

//     INSERT PSEUDOCODE
// Push the value into the values property on the heap
// Bubble Up:
// Create a variable called index which is the length of the values property - 1
// Create a variable called parentIndex which is the floor of (index-1)/2
// Keep looping as long as the values element at the parentIndex is less than the values element at the child index
// Swap the value of the values element at the parentIndex with the value of the element property at the child index
// Set the index to be the parentIndex, and start over!

    insert(element){
        this.values.push(element);
        this.bubbleUp();
    }
    bubbleUp(){
        let idx = this.values.length - 1;
        const element = this.values[idx];
        while(idx > 0){
            let parentIdx = Math.floor((idx - 1)/2);
            let parent = this.values[parentIdx];
            if(element <= parent) break;
            this.values[parentIdx] = element;
            this.values[idx] = parent;
            idx = parentIdx;
        }
    }
}

let heap = new MaxBinaryHeap();
heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
heap.insert(55);


// node stacks/binary-heap.js

