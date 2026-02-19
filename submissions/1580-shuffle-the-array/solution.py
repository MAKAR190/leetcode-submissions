class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * len(nums)
        j = 0

        for i in range(n):
            ans[j] = nums[i]
            ans[j + 1] = nums[i + n]
            j += 2
            
        return ans

