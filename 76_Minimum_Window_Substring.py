# cách tự làm
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         m = len(s)
#         n = len(t)

#         if m < n:
#             return ''

#         start = end = 0
#         character_in_t = dict()
#         minimum_window_substring = s
#         window_substring = ''
#         missing_character_quantity = n
#         is_s_include_every_characters_in_t = False
#         for character in t:
#             if character not in character_in_t:
#                 character_in_t[character] = [1, 0]
#             else:
#                 character_in_t[character][0] += 1

#         while end <= m:
#             if missing_character_quantity == 0:
#                 if len(window_substring) <= len(minimum_window_substring):
#                     is_s_include_every_characters_in_t = True
#                     minimum_window_substring = window_substring
#                 if s[start] in character_in_t:
#                     if character_in_t[s[start]][1] <= character_in_t[s[start]][0]:
#                         missing_character_quantity += 1
#                     character_in_t[s[start]][1] -= 1
#                 start += 1
#                 window_substring = window_substring[1:]
#                 continue
#             if end == m:
#                 break
#             if s[end] in character_in_t:
#                 if character_in_t[s[end]][1] < character_in_t[s[end]][0]:
#                     missing_character_quantity -= 1
#                 character_in_t[s[end]][1] += 1

#             window_substring += s[end]
#             end += 1
#         if not is_s_include_every_characters_in_t:
#             return ''
#         return minimum_window_substring

# cách trên mạng
import math
from collections import defaultdict


class Solution:
    def minWindow(self, s, t):
        ans, l = (0, math.inf), 0
        required, count = defaultdict(int), len(t)
        for letter in t:
            required[letter] += 1

        for r in range(len(s)):
            # Increment count, required, and r until window exists
            if 0 < required[s[r]]:
                count -= 1
            required[s[r]] -= 1
            if count == 0:
                # Decrement l until window is minimal
                while required[s[l]] < 0:
                    required[s[l]] += 1
                    l += 1
                ans = min(ans, (l, r), key=lambda x: x[1] - x[0])
                count += 1
                required[s[l]] += 1
                l += 1

        return '' if ans[1] == math.inf else s[ans[0]: ans[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"
so = Solution()
print(so.minWindow(s, t))
