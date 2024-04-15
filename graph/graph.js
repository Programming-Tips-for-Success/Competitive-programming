// Working with
// map/location data?
// Use a graph!

// A graph data structure consists of a finite (and possibly mutable) set of vertices or nodes or points, together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph.

// USES FOR GRAPHS
// Social Networks
// Location / Mapping
// Routing Algorithms
// Visual Hierarchy
// File System Optimizations

// Recommendations
// "People also watched"
// "You might also like..."
// "People you might know"
// "Frequently bought With

// ESSENTIAL GRAPH TERMS
// Vertex - a node
// Edge - connection between nodes
// Weighted/Unweighted - values assigned to distances between vertices
// Directed/Undirected - directions assigned to distanced between vertices

class Graph {
    #vertices = new Set();
    #adjacentList = new Map();
    
    get vertices() {
      return Array.from(this.#vertices)
    }
    
    get adjacentList() {
      const list = {};
      
      this.#adjacentList.forEach((val, key) => {
        list[key] = Array.from(val)
      })
      
      return list
    }

    addVertex(vertex = null) {
        if(
         !this.#vertices.has(vertex) &&
         vertex !== null && 
         vertex !== undefined
        ) {
          this.#vertices.add(vertex);
          this.#adjacentList.set(vertex, new Set());
        }
      }

      addEdge(vertex1 = null, vertex2 = null, directed = true) {
        if(
          vertex1 !== null && vertex1 !== undefined &&
          vertex2 !== null && vertex2 !== undefined && 
          vertex1 != vertex2
        ) {
          this.addVertex(vertex1);
          this.addVertex(vertex2);
          this.#adjacentList.get(vertex1).add(vertex2);
          if(directed) {
            this.#adjacentList.get(vertex2).add(vertex1);
          }
        }
      }
  }

  // For this graph, we will use the concept of colors to track whether we are done checking a node adjacency list or not and to avoid visiting a node more than once for efficiency. by default all nodes are green, when you check a node it becomes yellow and when you visit all its adjacent nodes it becomes red.
const COLORS = Object.freeze({
  GREEN: 'green',
  YELLOW: 'yellow',
  RED: 'red'
});
  
function breathFirstSearch(graph, fromVertex, callback) {
  const {vertices, adjacentList} = graph;
  
  if(vertices.length === 0) return;
  
  const color = vertices
      .reduce((c, v) => ({...c, [v]: COLORS.GREEN}), {});
  const queue = [];
  
  queue.push(fromVertex);
  
  while(queue.length) {
    const v = queue.shift();
    const nearVertex = adjacentList[v];
    color[v] = COLORS.YELLOW;
    
    nearVertex.forEach(w => {
      if(color[w] === COLORS.GREEN) {
        color[v] = COLORS.YELLOW;
        queue.push(w);
      }
    });
    
    color[v] = COLORS.RED;
    console.log(nearVertex);
    callback && callback(v);
  }
}

function depthFirstSearch(graph, fromVertex, callback) {
  const {vertices, adjacentList} = graph;
  
  if(vertices.length === 0) return;
  
  const color = vertices
      .reduce((c, v) => ({...c, [v]: COLORS.GREEN}), {});
  
  callback && callback(fromVertex);
  color[fromVertex] = COLORS.YELLOW;
  
  function visit(v) {
    if(color[v] === COLORS.GREEN) {
      callback && callback(v);
      color[v] = COLORS.YELLOW;
      adjacentList[v].forEach(visit);
    }
    color[v] = COLORS.RED;
  }
  
  adjacentList[fromVertex].forEach(visit);
}

  let list = new Graph();
  list.addVertex(1);
  list.addVertex(2);
  list.addVertex(3);
  list.addVertex(4);

  list.addEdge(1, 3);
  list.addEdge(1, 2);
  list.addEdge(1, 4);

  list.addEdge(2 ,1);
  list.addEdge(2, 3);

  list.addEdge(3, 2);
  list.addEdge(3, 4);
  list.addEdge(3, 1);

  list.addEdge(4, 1);
  list.addEdge(4, 3);

console.log(list.adjacentList, 'adjacentList');

breathFirstSearch(list, 1);
// node graph/graph.js