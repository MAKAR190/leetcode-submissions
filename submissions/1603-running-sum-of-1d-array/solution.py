class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      
        prefixes = [nums[0]]
        n = len(nums)
    
        for i in range(1, n):
            prefixes.append(prefixes[-1] + nums[i])

        return prefixes
