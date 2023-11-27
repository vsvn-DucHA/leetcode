from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        # print(piles)
        return sum(piles[1:-len(piles)//3:2])
    
piles = [9,8,7,6,5,1,2,3,4]
s=Solution()
print(s.maxCoins(piles))