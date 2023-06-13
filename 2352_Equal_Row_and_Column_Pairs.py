from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hashMap = defaultdict(int)

        for row in grid:
            rowStr = str(row)
            hashMap[rowStr] += 1

        count = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            colStr = str(col)
            count += hashMap[colStr]

        return count


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
s = Solution()
print(s.equalPairs(grid))
