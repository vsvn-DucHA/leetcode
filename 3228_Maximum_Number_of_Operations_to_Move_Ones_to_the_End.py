class Solution:
    def maxOperations(self, s: str) -> int:
        count_ones = 0
        max_operations = 0
        s += "1"
        for i, char in enumerate(s[:-1]):
            print(f"{char=} - {count_ones=} - {max_operations=}")
            if char == "1":
                count_ones += 1
            elif char == "0":
                if s[i + 1] == "0":
                    continue
                else:
                    max_operations += count_ones
        return max_operations


s = Solution()
print(s.maxOperations("1100"))
print(s.maxOperations("1001101"))
