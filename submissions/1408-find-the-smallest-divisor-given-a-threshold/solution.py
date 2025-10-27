class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            t = 0
            for num in nums:
                t += ceil(num / divisor)
            return t <= threshold
        
        
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = left  + (right - left) // 2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
