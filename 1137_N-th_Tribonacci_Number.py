class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]
        if n < 3:
            return res[n]
        for _ in range(n-2):
            res[0], res[1], res[2] = res[1], res[2], sum(res)
        return res[2]


s = Solution()
print(s.tribonacci(25))
