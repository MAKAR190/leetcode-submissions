# Approach

# 1. Write a bisec algo which explores first occurrence of a duplicatetarget -> O(log n)
# 2. Write a bisec algo which explores last occurrence of a duplicate target -> O(log n)
# 3. Consider two edge cases: when you can't find the target, you must return [-1, -1]
# And target could not be a duplicate, so we could return the same position twice, but still I guess we need to run two bisecs algos in order to get this one, because it is impossible otherwise to understand whether it is a duplicate or not using only binary search

# But we could also try to use two pointers technique, but that would be already out of our desirable TC, so we will just consider this brute-force solution



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = [-1, -1]
        
        if n == 0:
            return res
        
        def bisec_left(target):
            left = 0
            right = n
    
            while left < right:
                middle = (left + right) // 2
        
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
                    
            if left < n and nums[left] == target:
                res[0] = left
            

        def bisec_right(target):
            left = 0
            right = n
    
            while left < right:
                middle = (left + right) // 2
        
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle
                    
            if left > 0 and nums[left - 1] == target:
                res[1] = left - 1
    
        bisec_left(target)
        bisec_right(target)
        
        return res
        
        
