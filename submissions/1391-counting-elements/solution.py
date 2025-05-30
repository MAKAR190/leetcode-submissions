class Solution:
    def countElements(self, arr: List[int]) -> int: # [1,2,3]
        ans = 0
        s = set(arr)
    
        for num in arr:
            if num + 1 in s:
                ans +=1
        
        return ans
