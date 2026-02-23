class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        check = set()
        count = 0
        for i in range(len(s) - k + 1):
            if s[i : i + k] not in check:
                count += 1
                check.add(s[i : i + k])
        # print(check, count)
        return count == 2**k


s = Solution()
i = "00000000001011100"
k = 3
print(s.hasAllCodes(i, k))
