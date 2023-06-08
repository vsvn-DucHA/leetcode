from typing import List


class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(curr: List[int], i: int, s: int):
            if s == target:
                res.append(curr)
            elif s < target:
                for j in range(i, len(can)):
                    backtracking(curr+[can[j]], j, s+can[j])
        backtracking([], 0, 0)
        return res


s = Solution()
c = [10, 1, 2, 7, 6, 1, 5]
t = 8
print(s.combinationSum(c, t))
