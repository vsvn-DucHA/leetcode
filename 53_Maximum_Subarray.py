from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        sum_list=0
        for i in nums:
            if sum_list<0:
                sum_list=i
            else: 
                sum_list+=i
            if(max_sum<sum_list):
                max_sum=sum_list
        return max_sum 

nums=[-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(nums))