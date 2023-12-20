from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        leftover_money=money-sum(sorted(prices)[0:2])
        return  leftover_money if leftover_money>=0 else money
    
# bài nâng cao tự nghĩ ra là tìm 2 số để sao cho tiền còn dư là nhỏ nhất( đề bài cũ là mua 2 kẹo trong danh sách kẹo sao cho số dư >=0)
# class Solution:
#     def buyChoco(self, prices: List[int], money: int) -> int:
#         s,e=0,len(prices)-1
#         prices.sort()
#         leftover_money=money-(prices[0]+prices[1])
#         if leftover_money<0: return money
#         while(prices[s]+prices[e]>money):
#             e-=1
#         leftover_money=money-(prices[s]+prices[e])
#         while leftover_money>0 and s!=e-1:
#             if leftover_money+prices[s]-prices[s+1]>=0:
#                 leftover_money=leftover_money+prices[s]-prices[s+1]
#                 s+=1
#             else:
#                 leftover_money=leftover_money+prices[e]-prices[e-1]
#                 e-=1
                
#         return  prices[s],prices[e]
    
# prices=[1,2,4,4,5,5,11,20]
# money=10
# s=Solution()
# print(s.buyChoco(prices,money))