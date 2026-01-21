class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        # 1. Find pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # 2. If no pivot, reverse entire array
        if pivot == -1:
            nums.reverse()
            return

        # 3. Find rightmost successor
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break

        # 4. Reverse suffix (in-place)
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

