
#A,B,C,D,E
graph = {'A':
       ['B','C','D'],
       'B':['E'],
       'C':['D','E'],
       'D':[],
       'E':[]}
visited = []
def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        for nod in graph[node]:
            dfs(graph, visited, nod)
    return visited
visted = dfs(graph, visited, 'A')
print(visted)
        
