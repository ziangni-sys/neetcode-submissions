class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            array = nums[:i] + nums[i+1:]
            array.sort()
            #print(array)
            target = - nums[i]
            j = 0
            k = len(array) - 1
            while j < k:
                if array[j] + array[k] == target:
                    result.append([nums[i], array[j], array[k]])
                    j += 1
                    k -= 1
                elif array[j] + array[k] < target:
                    j += 1
                else:
                    k -= 1
        rset = set()
        resultf = []
        for r in result:
            if tuple(sorted(r)) not in rset:
                rset.add(tuple(sorted(r)))
                resultf.append(sorted(r))

        return resultf     
