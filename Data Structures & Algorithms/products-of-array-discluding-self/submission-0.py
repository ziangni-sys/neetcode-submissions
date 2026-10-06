class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefices = [1] * len(nums)
        suffices = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            prefices[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            suffices[i] = suffix
            suffix *= nums[i]
        for i in range(len(nums)):
            res[i] = prefices[i] * suffices[i]
        return res