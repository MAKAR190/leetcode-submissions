# Defining the problem
# We need somehow to split the array optimally (which means to find the largest acceptable sum for eac subarray) given that we need to have k subarrays

# Edge case (BINARY SEARCH)
# 

# Approach
# Binary Search on solution sapce + greedy check (check whether our target is suitable for k splits, if yes, try less one, if not suitable, increment to the most suitable target value)
# Solution space: minimum possible sum of subarray (which is the maximum element from the entire array)
# and maximum possible sum of the array

# TC and SC
# TC(n * log n) and SC(1)

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(target):
            curr_sum = 0
            splits = 0
            
            for num in nums:
                if curr_sum + num <= target:
                    curr_sum += num
                else:
                    curr_sum = num
                    splits += 1
                    
            return splits + 1 <= k
            
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
