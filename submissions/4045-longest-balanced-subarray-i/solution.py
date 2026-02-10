class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0

        for left in range(len(nums)):
            if ans == len(nums):
                break
                
            even_count = {}
            odd_count = {}

            for right in range(left, len(nums)):
                num = nums[right]

                if num % 2 == 0:
                    even_count[num] = even_count.get(num, 0) + 1
                else:
                    odd_count[num] = odd_count.get(num, 0) + 1

                if len(even_count.keys()) == len(odd_count.keys()):
                    ans = max(ans, right - left + 1)
            
        return ans
