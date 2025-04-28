class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        ans = curr / k  

        for right in range(k, len(nums)):
            curr += nums[right] - nums[right - k] 
            ans = max(ans, curr / k)
        
        return ans
