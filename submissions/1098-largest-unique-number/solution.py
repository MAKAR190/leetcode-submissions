class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = -1
        
        for num in nums:
            counts[num] += 1
        
        for num, appearance in counts.items():
            if appearance == 1:
                ans = max(ans, num)
                
        
        return ans
