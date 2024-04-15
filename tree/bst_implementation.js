class Node {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor(){
        this.root = null;
    }
    insert(value){
        var newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
            return this;
        }
        var current = this.root;
        while(true){
            if(value === current.value) return undefined;
            if(value < current.value){
                if(current.left === null){
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if(current.right === null){
                    current.right = newNode;
                    return this;
                } 
                current = current.right;
            }
        }
    }
    find(value){
        if(this.root === null) return false;
        var current = this.root,
            found = false;
        while(current && !found){
            if(value < current.value){
                current = current.left;
            } else if(value > current.value){
                current = current.right;
            } else {
                found = true;
            }
        }
        if(!found) return undefined;
        return current;
    }
    contains(value){
        if(this.root === null) return false;
        var current = this.root,
            found = false;
        while(current && !found){
            if(value < current.value){
                current = current.left;
            } else if(value > current.value){
                current = current.right;
            } else {
                return true;
            }
        }
        return false;
    }

      BFS(){
        var node = this.root,
            data = [],
            queue = [];
        queue.push(node);

        while(queue.length){
           node = queue.shift();
           data.push(node.value);
           if(node.left) queue.push(node.left);
           if(node.right) queue.push(node.right);
        }
        return data;
    }

     DFSPreOrder(){
        var data = [];
        function traverse(node){
            data.push(node.value);
            if(node.left) traverse(node.left);
            if(node.right) traverse(node.right);
        }
        traverse(this.root);
        return data;
    }
    DFSPostOrder(){
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            if(node.right) traverse(node.right);
            data.push(node.value);
        }
        traverse(this.root);
        return data;
    }
    DFSInOrder(){
        var data = [];
        function traverse(node){
            if(node.left) traverse(node.left);
            data.push(node.value);
            if(node.right) traverse(node.right);
        }
        traverse(this.root);
        return data;
    }
}

function print(x){
console.log(x);

}
//      10
//   5     13
// 2  7  11  16

var tree = new BinarySearchTree();
// tree.insert(10)
// tree.insert(5)
// tree.insert(13)
// tree.insert(11)
// tree.insert(2)
// tree.insert(16)
// tree.insert(7)
// tree.BFS();
// print(tree);

// tree.insert(15); // new tree
// tree.insert(20);
// tree.insert(10);
// tree.insert(12);
// print(tree.root.value) // 15
// print(tree.root.right.value) // 20
// tree.root.left.right.value // 12
 
// tree
//     .insert(15)
//     .insert(20)
//     .insert(10)
//     .insert(12);
// tree.root.value // 15
// tree.root.right.value // 20
// print(tree.root.left.right.value) // 12

// tree
//     .insert(15)
//     .insert(20)
//     .insert(10)
//     .insert(12);
// var foundNode = tree.find(20);
// print(foundNode.value) // 20
// foundNode.left // null
// foundNode.right // null
 

// tree
//     .insert(15)
//     .insert(20)
//     .insert(10)
//     .insert(12);
// var foundNode = tree.find(120);
// foundNode // undefined


tree
    .insert(15)
    .insert(20)
    .insert(10)
    .insert(12)
    .insert(1)
    .insert(5)
    .insert(50);
tree.DFSPreOrder() // [15, 10, 1, 5, 12, 20, 50]


tree
    .insert(15)
    .insert(20)
    .insert(10)
    .insert(12)
    .insert(1)
    .insert(5)
    .insert(50);
tree.DFSInOrder() // [1, 5, 10, 12, 15, 20, 50]



tree
    .insert(15)
    .insert(20)
    .insert(10)
    .insert(12)
    .insert(1)
    .insert(5)
    .insert(50);
tree.DFSPostOrder() // [5, 1, 12, 10, 50, 20, 15]

// node tree/bst_implementation.js



