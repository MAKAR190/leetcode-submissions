class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            s.add(num)
            
        
        for check in range(0, len(nums) + 1):
            if not check in s:
                return check
        
        return -1
