# Defining the problem
# We need to iterate fast using 3 variables in order to satisfy a condition, which is satisfied when those 3 variables - the triplet - sums up to 0 (meaning the elements, not indices) and there cannot be any duplicates

# Edge cases


# Approach
# I guess we could iterate twice for more optimal approach (better than iterating 3 times)
# So, first loop would pick i as it is
# And second one would use two pointers
# So the when all elements sums up to 0, we push it into the answer (list)
# Then we should somehow check before even comparing or inserting into the answer whether it is a duplicate triplet or not
# We could use a set where the indicies of those triplets which have been already used will be stored, but then we would need to somehow check each time before inserting or comparing so it wouldn't take too much time
# We could use sorting them in order and when checking those indices before inserting sorting them as well. But it would take n * log n time, which means we are not at n**2 solution, but n**2*logn. But we could try that as our first brute-force solution and then try to optimize

# Time Complexity and Space Complexity
# TC(n**2*logn)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n - 2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                
                j = i + 1
                k = n - 1

                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:                        
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        j += 1
        
        return ans
        
