from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        onceTime = dict()
        for i in nums:
            if i in onceTime:
                onceTime[i] = False
            else:
                onceTime[i] = True
        for i in onceTime:
            if onceTime[i] == True:
                return i
        return 0


nums = [0, 1, 0, 1, 0, 1, 99]


s = Solution()
print(s.singleNumber(nums))
