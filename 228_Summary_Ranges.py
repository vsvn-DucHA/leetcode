from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end = 0, 0
        results = []
        n = len(nums)
        if end == n:
            return []
        while end < n:
            if end == n-1:
                results.append(
                    f'{nums[start]}->{nums[end]}' if start != end else str(nums[start]))
                return results

            if nums[end] != nums[end+1]-1:
                results.append(
                    f'{nums[start]}->{nums[end]}' if start != end else str(nums[start]))
                start = end = end+1
            else:
                end += 1
        if start == n-1:
            results.append(str(nums[start]))
        return results


nums = [0, 1, 2, 4, 5, 7]
s = Solution()
print(s.summaryRanges(nums))
