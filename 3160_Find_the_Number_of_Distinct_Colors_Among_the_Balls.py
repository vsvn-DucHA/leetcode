from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors = defaultdict(int)
        balls = defaultdict(int)
        for [ball, color] in queries:
            if balls[ball]:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    del colors[balls[ball]]
            colors[color] += 1
            balls[ball] = color
            res.append(len(colors))
        return res


s = Solution()
limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
print(s.queryResults(limit, queries))
