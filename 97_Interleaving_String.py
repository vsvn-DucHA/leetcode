import numpy as np
class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     m, n, l = len(s1), len(s2), len(s3)
    #     if m + n != l:
    #         return False
        
    #     dp = [[False] * (n + 1) for _ in range(m + 1)]
    #     dp[0][0] = True
    #     dp=np.array(dp)
    #     for i in range(1, m + 1):
    #         dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    #     print(dp)
    #     for j in range(1, n + 1):
    #         dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    #     print(dp)
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    #     print(dp)
    #     return dp[m][n]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        minLength=min(m,n)
        if m + n != l:
            return False
        dp=[[False]*(minLength+1) for i in range(2)]
        dp=np.array(dp)
        
        print(dp)
        return True
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s=Solution()
print(s.isInterleave(s1,s2,s3))