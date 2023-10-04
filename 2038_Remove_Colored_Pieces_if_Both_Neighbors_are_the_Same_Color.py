
import re


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_plays = sum(len(match.group()) - 2 for match in re.finditer(r'A{3,}', colors))
        
        bob_plays = sum(len(match.group()) - 2 for match in re.finditer(r'B{3,}', colors))
        for match in re.finditer(r'B{3,}', colors):
            print(match.group())
        return alice_plays > bob_plays
s=Solution()
colors = "ABBBBBBBAAA"
print(s.winnerOfGame(colors))