class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k > 0 else stack

        result = ''.join(stack).lstrip('0')

        return result if result else '0'


s = Solution()
nums = [['1432219', 3], ['10200', 1], ['10', 2],
        ['112', 1], ['10001', 4], ['1234567890', 9]]
nums = [['1432219', 3]]
for item in nums:
    print(s.removeKdigits(*item))
