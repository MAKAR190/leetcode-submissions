class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        index = right
        
        numsSorted = [0] * len(nums)
        
        while left <= right:
            leftSquare = nums[left] ** 2
            rightSquare = nums[right] ** 2
            
            if leftSquare > rightSquare:
                numsSorted[index] = leftSquare
                left += 1
            else:
                numsSorted[index] = rightSquare
                right -= 1
            
            index -= 1
            
        return numsSorted
