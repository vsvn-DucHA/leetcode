class Solution:
    def smallestNumber(self, n: int) -> int:
        while n & (n + 1):
            n |= n + 1
        return n


s = Solution()
print(s.smallestNumber(1))
print(s.smallestNumber(2))
print(s.smallestNumber(5))
print(s.smallestNumber(4))
print(s.smallestNumber(10))
