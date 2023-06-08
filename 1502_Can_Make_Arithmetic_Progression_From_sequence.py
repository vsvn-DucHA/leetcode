import math
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        min = max = arr[0]
        for i in arr:
            if i < min:
                min = i
            if i > max:
                max = i
        d = (max-min)/(n-1)
        if d == 0:
            return True
        elif d-math.floor(d) != 0:
            return False
        else:
            sum = 0
            multiplesList = dict()
            for i in arr:
                sum += i
                if (i-min) % d != 0:
                    return False
                if i in multiplesList:
                    return False
                else:
                    multiplesList[i] = i
            if sum != n*min+n*(n-1)/2*d:
                return False
            return True


nums = [1, 2, 2, 5, 5]


s = Solution()
print(s.canMakeArithmeticProgression(nums))
