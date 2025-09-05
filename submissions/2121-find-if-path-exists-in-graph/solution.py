from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list) 
        seen = {source} 
        
        for [x, y] in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            if node == destination: 
                return True
            
            for neighbour in graph[node]:
                if neighbour not in seen: 
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False
        
        return dfs(source)
                
            
