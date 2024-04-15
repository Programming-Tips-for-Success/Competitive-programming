// WE ARE BUILDING AN UNDIRECTED GRAPH




// ADDING A VERTEX
// Write a method called addVertex, which accepts a name of a vertex
// It should add a key to the adjacency list with the name of the vertex and set its value to be an empty array

// g.addVertex("Tokyo")
// o/p
// {
//     "Tokyo": []
// }

// ADDING AN EDGE
// This function should accept two vertices, we can call them vertex1 and vertex2
// The function should find in the adjacency list the key of vertex1 and push vertex2 to the array
// The function should find in the adjacency list the key of vertex2 and push vertex1 to the array
// Don't worry about handling errors/invalid vertices

// g.addEdge("Tokyo", "Dallas")
// o/p
// {
//   "Tokyo": ["Dallas"],
//   "Dallas": ["Tokyo"],
//   "Aspen": []
// }

// REMOVING AN EDGE
// This function should accept two vertices, we'll call them vertex1 and vertex2
// The function should reassign the key of vertex1 to be an array that does not contain vertex2
// The function should reassign the key of vertex2 to be an array that does not contain vertex1
// Don't worry about handling errors/invalid vertices

// g.removeEdge("Tokyo", "Dallas")
// o/p
// {
//   "Tokyo": [],
//   "Dallas": ["Aspen"],
//   "Aspen": ["Dallas"]
// }

// REMOVING A VERTEX
// The function should accept a vertex to remove
// The function should loop as long as there are any other vertices in the adjacency list for that vertex
// Inside of the loop, call our removeEdge function with the vertex we are removing and any values in the adjacency list for that vertex
// delete the key in the adjacency list for that vertex

// {
//   "Tokyo": ["Dallas", "Hong Kong"],
//   "Dallas": ["Tokyo", "Aspen", "Hong Kong", "Los Angeles"],
//   "Aspen": ["Dallas"],
//   "Hong Kong": ["Tokyo", "Dallas", "Los Angeles"],
//   "Los Angeles": ["Hong Kong", "Dallas"]
// }
// g.removeVertex("Hong Kong")
// o/p
// {
//   "Tokyo": ["Dallas"],
//   "Dallas": ["Tokyo", "Aspen","Los Angeles"],
//   "Aspen": ["Dallas"],
//   "Los Angeles": ["Dallas"]
// }

// GRAPH TRAVERSAL USES
// Peer to peer networking
// Web crawlers
// Finding "closest" matches/recommendations
// Shortest path problems
// GPS Navigation
// Solving mazes
// AI (shortest path to win the game

// DEPTH FIRST
// Explore as far as possible down one branch before "backtracking"

// DFS PSEUDOCODE
// Recursive
//  DFS(vertex):
//     if vertex is empty
//         return (this is base case)
//     add vertex to results list
//     mark vertex as visited
//     for each neighbor in vertex's neighbors:
//        if neighbor is not visited:
//           recursively call DFS on neighbor

// DEPTH FIRST TRAVERSAL 
// The function should accept a starting node

// Create a list to store the end result, to be returned at the very end

// Create an object to store visited vertices

// Create a helper function which accepts a vertex

// The helper function should return early if the vertex is empty

// The helper function should place the vertex it accepts into the visited object and push that vertex into the result array.

// Loop over all of the values in the adjacencyList for that vertex

// If any of those values have not been visited, recursively invoke the helper function with that vertex

// Invoke the helper function with the starting vertex

// Return the result array

// DFS-iterative(start):
//     let S be a stack
//     S.push(start)
//     while S is not empty
//         vertex = S.pop()
//         if vertex is not labeled as discovered:
//             visit vertex (add to result list)
//             label vertex as discovered
//             for each of vertex's neighbors, N do 
//                 S.push(N)

// DEPTH FIRST TRAVERSAL  - iterative
// The function should accept a starting node

// Create a stack to help use keep track of vertices (use a list/array)

// Create a list to store the end result, to be returned at the very end

// Create an object to store visited vertices

// Add the starting vertex to the stack, and mark it visited

// While the stack has something in it:

// Pop the next vertex from the stack

// If that vertex hasn't been visited yet:

// ​Mark it as visited

// Add it to the result list

// Push all of its neighbors into the stack
// Return the result array

// DEPTH FIRST TRAVERSAL
// The function should accept a starting node
// Create an object to store visited nodes and an array to store the result
// Create a helper function which accepts a vertex
// The helper function should place the vertex it accepts into the visited object and push that vertex into the results
// Loop over all of the values in the adjacencyList for that vertex
// If any of those values have not been visited, invoke the helper function with that vertex
// return the array of results


// BREADTH FIRST
// Visit neighbors at current depth first!

// This function should accept a starting vertex
// Create a queue (you can use an array) and place the starting vertex in it
// Create an array to store the nodes visited
// Create an object to store nodes visited
// Mark the starting vertex as visited
// Loop as long as there is anything in the queue
// Remove the first vertex from the queue and push it into the array that stores nodes visited
// Loop over each vertex in the adjacency list for the vertex you are visiting.
// If it is not inside the object that stores nodes visited, mark it as visited and enqueue that vertex
// Once you have finished looping, return the array of visited nodes

class Graph{
    constructor(){
        this.adjacencyList = {};
    }
    addVertex(vertex){
        if(!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
    }

      addEdge(v1,v2){
        this.adjacencyList[v1].push(v2);
        this.adjacencyList[v2].push(v1);
    }

       removeEdge(vertex1,vertex2){
        this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(
            v => v !== vertex2
        );
        this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(
            v => v !== vertex1
        );
    }

      removeVertex(vertex){
        while(this.adjacencyList[vertex].length){
            const adjacentVertex = this.adjacencyList[vertex].pop();
            this.removeEdge(vertex, adjacentVertex);
        }
        delete this.adjacencyList[vertex]
    }

        depthFirstRecursive(start){
        const result = [];
        const visited = {};
        const adjacencyList = this.adjacencyList;

        (function dfs(vertex){
            if(!vertex) return null;
            visited[vertex] = true;
            result.push(vertex);
            adjacencyList[vertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    return dfs(neighbor)
                }
            });
        })(start);

        return result;
    }

      depthFirstIterative(start){
        const stack = [start];
        const result = [];
        const visited = {};
        let currentVertex;

        visited[start] = true;
        while(stack.length){
            currentVertex = stack.pop();
            result.push(currentVertex);

            this.adjacencyList[currentVertex].forEach(neighbor => {
               if(!visited[neighbor]){
                   visited[neighbor] = true;
                   stack.push(neighbor)
               } 
            });
        }
        return result;
    }

        breadthFirst(start){
        const queue = [start];
        const result = [];
        const visited = {};
        let currentVertex;
        visited[start] = true;

        while(queue.length){
            currentVertex = queue.shift();
            result.push(currentVertex);
           

            this.adjacencyList[currentVertex].forEach(neighbor => {
                if(!visited[neighbor]){
                    visited[neighbor] = true;
                    queue.push(neighbor);
                }
            });
        }
        return result;
    }
}

function print(x){
console.log(x);
}

let g = new Graph();
// g.addVertex("Dallas");
// g.addVertex("Tokyo");
// g.addVertex("Aspen");
// g.addEdge("Dallas", "Tokyo");
// g.addEdge("Dallas", "Aspen");
// g.addEdge("Hong Kong", "Tokyo");
// g.addEdge("Hong Kong", "Dallas");
// g.addEdge("Los Angeles", "Hong Kong");
// g.addEdge("Los Angeles", "Aspen");

// g.addVertex("A")
// g.addVertex("B")
// g.addVertex("C")
// g.addVertex("D")
// g.addVertex("E")
// g.addVertex("F")


// g.addEdge("A", "B")
// g.addEdge("A", "C")
// g.addEdge("B","D")
// g.addEdge("C","E")
// g.addEdge("D","E")
// g.addEdge("D","F")
// g.addEdge("E","F")
// g.depthFirstRecursive("A")

//          A
//        /   \
//       B     C
//       |     |
//       D --- E
//        \   /
//          F

// graph.adjacencyList['A']; // contains both ('B', 'C')
// graph.adjacencyList['B']; // contains both ('A', 'D')
// graph.adjacencyList['C']; // contains both ('A', 'D')
// graph.adjacencyList['D']; // contains both ('C', 'B')

g.addVertex('S');
g.addVertex('P');
g.addVertex('U');
g.addVertex('X');
g.addVertex('Q');
g.addVertex('Y');
g.addVertex('V');
g.addVertex('R');
g.addVertex('W');
g.addVertex('T');
 
g.addEdge('S','P');
g.addEdge('S','U');
 
g.addEdge('P','X');
g.addEdge('U','X');
 
g.addEdge('P','Q');
g.addEdge('U','V');
 
g.addEdge('X','Q');
g.addEdge('X','Y');
g.addEdge('X','V');
 
g.addEdge('Q','R');
g.addEdge('Y','R');
 
g.addEdge('Y','W');
g.addEdge('V','W');
 
g.addEdge('R','T');
g.addEdge('W','T');
 
print(g.breadthFirst('S')); // ["S", "P", "U", "X", "Q", "V", "Y", "R", "W", "T"]

// node graph/graph_class.js
