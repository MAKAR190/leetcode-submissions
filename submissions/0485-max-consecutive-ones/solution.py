class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = curr = 0
        
        for num in nums:
            if num == 1:
                curr += 1
                ans = max(ans, curr)
            elif num == 0:
                curr = 0
                
        return ans


