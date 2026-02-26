class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        while s[-1] == "0":
            s = s[:-1]
            count += 1
        if s == "1":
            return count
        count += len(s)
        count += s.count("0") + 1 if s != "1" else 0
        return count


s = "1101"
print(Solution().numSteps(s))
