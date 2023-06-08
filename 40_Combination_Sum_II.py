from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtracking(curr, i, s):
            if s == target:
                ans.append(curr)
                return

            for j in range(i, len(candidates)):
                if s + candidates[j] > target:
                    return
                elif j > i and candidates[j] == candidates[j-1]:
                    continue
                else:
                    backtracking(curr + [candidates[j]], j + 1, s +
                                 candidates[j])

        backtracking([], 0, 0)
        return ans


s = Solution()
c = [2, 5, 2, 1, 2]
t = 5
print(s.combinationSum2(c, t))
