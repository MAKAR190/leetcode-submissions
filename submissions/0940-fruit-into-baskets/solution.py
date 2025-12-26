class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = ans = 0
        n = len(fruits)
        counts = {}
        
        for right in range(n):
            tree = fruits[right]
            counts[tree] = counts.get(tree, 0) + 1
                
            
            while len(counts) > 2:
                counts[fruits[left]] -= 1
                
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans
