from heapq import heappop, heappush
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        print(sorted(intervals))
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq)
            heappush(pq, right)
        return len(pq)


intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
s = Solution()
print(s.minGroups(intervals))
