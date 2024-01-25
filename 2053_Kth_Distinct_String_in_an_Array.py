from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq=dict()
        for s in arr:
            if s in freq:
                freq[s]+=1
            else:
                freq[s]=1
        for s,quality in freq.items():
            if quality==1:
                k-=1
                if(k==0):
                    return s 
        return ''
    

s=Solution()
arr =["d","b","c","b","c","a"]
k=2
print(s.kthDistinct(arr,k))