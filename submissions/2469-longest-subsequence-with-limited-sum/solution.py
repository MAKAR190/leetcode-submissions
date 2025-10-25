# O((n + m)* log n)
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(array, target):
            left, right = 0, len(array)
            
            while left < right:
                middle = (left + right) // 2
                
                if array[middle] > target:
                    right = middle
                else:
                    left = middle + 1
                
            return left
        
        ans = []
        nums.sort()
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for query in queries:
            index = binary_search(nums, query)
            ans.append(index)
        
        return ans
