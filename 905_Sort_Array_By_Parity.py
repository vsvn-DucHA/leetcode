from typing import List
from collections import deque

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=deque()
        for i in nums:
            if i%2==0:
                res.appendleft(i)
            else:
                res.append(i)
        return  res
    
s=Solution()
nums = [3,1,2,4]
print(s.sortArrayByParity(nums))