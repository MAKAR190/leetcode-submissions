class Solution:
     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        ans = []
        graph = {}

        for a, b in prerequisites:
            graph.setdefault(a, []).append(b)

        def dfs(node):
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            for neighbour in graph.get(node, []):
                if not dfs(neighbour):
                    return False
            path.remove(node)
            
            visited.add(node)
            ans.append(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return ans
