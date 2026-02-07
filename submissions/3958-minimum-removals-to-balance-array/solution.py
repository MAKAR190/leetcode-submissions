class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left = 0

        for right in range(n):
            if nums[right] <= k * nums[left]:
                continue
            
            left += 1
        
        return left
