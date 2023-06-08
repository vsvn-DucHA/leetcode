from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        return self.loop_subsets(nums, 0, [], [])

    def loop_subsets(self, nums: List[int], n: int, result: List[int], results: List[List[int]]) -> List[List[int]]:
        if n == len(nums):
            results.append(result.copy())
            return results
        for i in [0, 1]:
            if i == 1:
                result.append(nums[n])
                self.loop_subsets(nums, n+1, result, results)
                result.pop()
            else:
                self.loop_subsets(nums, n+1, result, results)

        return results


nums = [1, 2, 3]
s = Solution()
print(s.subsets(nums))
