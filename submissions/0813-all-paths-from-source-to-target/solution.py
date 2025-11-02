# How to do using backtracking and not just building a graph from edges list and using DFS?

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(curr):
            if curr[-1] == destination:
                ans.append(curr[:])
                return
            
            for neighbor in graph[curr[-1]]:
                if neighbor not in curr:
                    curr.append(neighbor)
                    backtrack(curr)
                    curr.pop()
                    
                
        n, destination = len(graph), len(graph) - 1
        ans = []
        backtrack([0])
        
        return ans
            
