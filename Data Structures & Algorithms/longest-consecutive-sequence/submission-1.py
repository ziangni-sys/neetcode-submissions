class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = [0] * len(nums)
        for i in range(len(nums)):
            k = nums[i]
            count[i] = 1
            while k+1 in nums:
                count[i] = count[i] + 1
                k = k + 1
        return 0 if len(count) == 0 else max(count)
            