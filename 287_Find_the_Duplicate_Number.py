from typing import List


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         count=dict()
#         for i in nums:
#             if i in count:
#                 return i
#             else:
#                 count[i]=1
#         return 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
s=Solution()
nums = [10,3,4,2,2]
print(s.findDuplicate(nums))   