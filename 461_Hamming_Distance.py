import random
import time


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def bitcount(n):
            count = 0
            while n > 0:
                count = count + 1
                n = n & (n-1)
            return count
        return bitcount(x^y)
    def hammingDistance1(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        while z > 0:
            count += z % 2
            z = z // 2
        return count
s=Solution()
t=time.time()
for i in range(int(1e7)):
    x=random.randint(1,int(1e8))
    y=random.randint(1,int(1e8))
    (s.hammingDistance(x,y))
print(time.time()-t)
t=time.time()
for i in range(int(1e7)):
    x=random.randint(1,int(1e8))
    y=random.randint(1,int(1e8))
    (s.hammingDistance1(x,y))
print(time.time()-t)
