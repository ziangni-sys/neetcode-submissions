class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue #-4 -1 -1 0 1 2 
            target = - nums[i]
            left = i + 1
            right = len(nums) - 1
            # >=3
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) - 1 and nums[left] == nums[left-1]:
                        left += 1
                        continue
                    while right > i + 1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res