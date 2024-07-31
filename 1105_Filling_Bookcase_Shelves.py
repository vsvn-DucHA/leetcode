from typing import List


class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)

        f = [0] * (n + 1)
        print(books)
        for i, (w, h) in enumerate(books, 1):
            print()
            print([w, h], "i:", i, "f:", f)
            f[i] = f[i - 1] + h

            for j in range(i - 1, 0, -1):
                print("j", j, w, books[j - 1], f)
                w += books[j - 1][0]

                if w > shelfWidth:

                    break

                h = max(h, books[j - 1][1])

                f[i] = min(f[i], f[j - 1] + h)
                print(f)

            print("f:", f)

        return f[n]


books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelfWidth = 4
s = Solution()
print(s.minHeightShelves(books, shelfWidth))
