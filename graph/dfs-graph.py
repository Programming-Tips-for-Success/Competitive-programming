# Depth First Traversal of a graph

visited = [] 
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph = { 
  'A' : ['B','C'], 
  'B' : ['D', 'E'], 
  'C' : ['F'], 
  'D' : [], 
  'E' : ['F'], 
  'F' : [] 
}
visited2 = set() # Set to keep track of visited nodes.
dfs(visited2, graph, 'A')