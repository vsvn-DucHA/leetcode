from heapq import heappop, heappush
from typing import List


def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}  
        min_heap = [(0, 0)]
        
        mst_weight = 0
        
        while min_heap:
            w, u = heappop(min_heap)
            print(w,u)
            if visited[u] or heap_dict.get(u, float('inf')) < w:
                continue
                
            visited[u] = True
            mst_weight += w
            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])
      
                    if new_distance < heap_dict.get(v, float('inf')):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))
            print(heap_dict)
            print(min_heap)
            print()
        return mst_weight
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
s=Solution()
print(s.minCostConnectPoints(points))
a=[]
heappush(a,(1,0))
heappush(a,(8,9))
heappush(a,(0,1))
print(a)