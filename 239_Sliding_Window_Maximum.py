from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums
        
        deq = deque()
        
        result = []
        for i in range(len(nums)):
            
            while deq and deq[0] < i - k + 1:
                deq.popleft()
            # print('lan 1:',i,deq)
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            # print('lan 2:',i,deq)
            
            deq.append(i)
            # print('lan 3:',i,deq)
            
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
s=Solution()
print(s.maxSlidingWindow(nums,k))