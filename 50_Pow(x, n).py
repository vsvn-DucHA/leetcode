class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            return self.myPow(1/x,-n)
        elif n%2==1:
            return self.myPow(x**2,n//2)*x
        else:
            return self.myPow(x**2,n//2)
        
    
    
x = 2.00000
n = -2147483648   
s=Solution()
print(s.myPow(x,n))