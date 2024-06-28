from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count_list = [0 for i in range(n)]
        for x, y in roads:
            count_list[x] += 1
            count_list[y] += 1
        count_list.sort()
        ans = 0
        for i in range(1, n + 1):
            ans += i * count_list[i - 1]
        return ans


s = Solution()
n = 5
roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
print(s.maximumImportance(n, roads))
