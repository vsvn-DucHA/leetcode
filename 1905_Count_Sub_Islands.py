from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid1), len(grid1[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.island_count = 0
        self.is_sub_island = True

        def dfs(r, c):
            if r < 0 or c < 0 or c >= col or r >= row or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0
            if grid1[r][c] == 0:
                self.is_sub_island = False
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)

            return self.is_sub_island

        for r in range(row):
            for c in range(col):
                if grid2[r][c] == 1:
                    self.is_sub_island = True

                    if dfs(r, c):
                        self.island_count += 1

        return self.island_count


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
s = Solution()
print(s.countSubIslands(grid1, grid2))
