from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        if numRows==1: return res
        res.append([1,1])
        if numRows==2: return res
        for i in range(2,numRows):
            subRes=[1]
            for j in range(1,i):
                subRes.append(res[i-1][j-1]+res[i-1][j])
            subRes.append(1)
            res.append(subRes)
        return res
    
s=Solution()
print(s.generate(5))