from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        i = 0
        # j = n-1
        j = len(grid[0])-1
        res = 0
        # while (i < m and j >= 0):
        while (i < len(grid) and j >= 0):
            if grid[i][j] < 0:
                # res += (m-i)
                res += (len(grid)-i)
                j -= 1
            else:
                i += 1
        return res


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

s = Solution()
print(s.countNegatives(grid))
