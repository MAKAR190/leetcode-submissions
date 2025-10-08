class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_distances = defaultdict(int)

        for i in range(len(nums)):
            ind_distance = target - nums[i]

            if nums[i] in ind_distances:
                return [ind_distances[nums[i]], i]

            ind_distances[ind_distance] = i    


