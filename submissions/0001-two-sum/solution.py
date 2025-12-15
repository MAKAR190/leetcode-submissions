from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = defaultdict(list)
        
        for i in range(len(nums)):
            curr_target = target - nums[i]

            if curr_target in remainders:
                return [remainders[curr_target][1], i]
            
            remainders[nums[i]] = [curr_target, i]

        return []               



