from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[]
        subres=dict()
        for index,size in enumerate(groupSizes):
            if size in subres:
                subres[size].append(index)
            else:
                subres[size]=[index]
            if size==len(subres[size]):
                res.append(subres.pop(size))
        return res
    
s=Solution()
groupSizes = [3,3,3,3,3,1,3]
print(s.groupThePeople(groupSizes))