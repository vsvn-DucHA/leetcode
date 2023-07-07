from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        for i in range(n - 1):
            accu = arr[i]
            for k in range(i + 1, n):
                accu ^= arr[k]
                if accu == 0:
                    res += k - i
        return res


arr = [2, 3, 1, 6, 7]
s = Solution()
print(s.countTriplets(arr))
