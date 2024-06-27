from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u1, v1 = edges[0]
        u2, v2 = edges[1]

        if u1 == u2 or u1 == v2:
            return u1
        else:
            return v1


edges = [[1, 2], [2, 3], [4, 2]]
s = Solution()
print(s.findCenter(edges))
