from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) in [1,2]:
            return True
        check=[0,0]
        for i in range(1,len(nums)):
            if (nums[i]-nums[i-1])<0:
                check[0]+=1
            if (nums[i]-nums[i-1])>0:
                check[1]+=1
            if check[0]*check[1]!=0:
                return False
        return True
    
s=Solution()
nums = [1,3,2]
print(s.isMonotonic(nums))