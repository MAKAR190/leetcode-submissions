from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def path_exists(src, target):
            visited[src] = True

            if src == target:
                return True

            for neighbor in graph[src]:
                if not visited[neighbor]:
                    if path_exists(neighbor, target):
                        return True

            return False
        
        n = len(edges)
        graph = defaultdict(list)

        for a, b in edges:
            visited = [False] * n
            u, v = a - 1, b - 1

            if path_exists(u, v):
                return [a, b]
            
            graph[u].append(v)
            graph[v].append(u)
        
        return []
