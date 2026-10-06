class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[n] = i