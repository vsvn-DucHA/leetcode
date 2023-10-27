from typing import List


MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        s = set(arr)
        dp = {x: 1 for x in arr}
        
        for i in arr:
            for j in arr:
                if j > i**0.5:
                    break
                if i % j == 0 and i // j in s:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    dp[i] %= MOD
        print(5//2)
        return sum(dp.values()) % MOD

arr=[2,4,5,10] 
s=Solution()
print(s.numFactoredBinaryTrees(arr))