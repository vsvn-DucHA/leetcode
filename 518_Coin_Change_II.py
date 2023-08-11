from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize the dp table with 0s
        dp = [0] * (amount+1)
        # There is 1 way to make 0 amount
        dp[0] = 1
        
        for coin in coins:
            # For each coin, update the dp table starting from the coin value
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        print(dp)
        return dp[amount]
    
    
amount = 10
coins = [1,2,5]
s=Solution()
print(s.change(amount,coins))