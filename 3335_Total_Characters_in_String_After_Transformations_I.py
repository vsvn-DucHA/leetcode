
class Solution:

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """Summary or Description of the Function
            cnt: là mảng 25 phần tử tương ứng theo vị trí : 0~a,1~b,...,25~z

            f(i,c) = số lần xuất hiện của c ở lần biến đổi thứ i

            c=0 -> f(i,0)=f(i-1,25)
            c=1 -> f(i,0)=f(i-1,25)+f(i-1,1)
            c>2 -> f(i,c)=f(i-1,c-1)

        """

        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        ans = sum(cnt) % mod
        return ans


so = Solution()
s = "jqktcurgdvlibczdsvnsg"
t = 7517
# print(so.lengthAfterTransformations(s, t))
print(ord('b')-ord('a'))
