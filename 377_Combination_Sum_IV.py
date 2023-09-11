from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=[]
        subRes=[]
        def backtracking(subTarget:int):
            if subTarget<0:
                return
            elif subTarget==0:
                res.append(subRes.copy())
                return 
            else:
                for i in nums:
                    subRes.append(i)
                    backtracking(subTarget-i)
                    subRes.pop()
        backtracking(target)
        return len(res) 
    
s=Solution()
nums = [1,2,4]
target = 32
print(s.combinationSum4(nums,target))