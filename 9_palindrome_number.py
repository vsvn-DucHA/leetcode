class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        if x < 0:
            return False
        elif x == 0:
            return True
        count = 0
        while x != 0:
            x //= 10
            count += 1
        return self.check_start_end(a, count)

    def check_start_end(self, x: int, length_x: int):
        if length_x in [0, 1]:
            return True
        else:
            a = x//10**(length_x-1)
            b = x % 10
            print(a, b)
            if a != b:
                return False
            else:
                return self.check_start_end((x-a*10**(length_x-1))//10, length_x-2)


solution = Solution()
print(solution.isPalindrome(-121))
# print(solution.check_start_end(1221, 4))
