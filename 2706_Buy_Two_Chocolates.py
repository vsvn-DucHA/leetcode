from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        leftover_money=money-sum(sorted(prices)[0:2])
        return  leftover_money if leftover_money>=0 else money