class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        start = 0
        current_cost = 0
        max_length = 0

        for end in range(n):
            current_cost += abs(ord(s[end]) - ord(t[end]))

            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_length = max(max_length, end - start + 1)
        return max_length


so = Solution()
# input = [['abcd', 'bcdf', 3], ['abcd', 'cdef', 3],
#          ['abcd', 'acde', 0], ['krrgw', 'zjxss', 19]]
input = [['krrgw', 'zjxss', 19]]
for s, t, maxCost in input:

    print(s, t, maxCost, so.equalSubstring(s, t, maxCost))
