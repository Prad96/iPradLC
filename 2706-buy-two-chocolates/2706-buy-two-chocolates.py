class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        chocolate1=min(prices)
        prices.remove(chocolate1)
        chocolate2=min(prices)
        balance=money-(chocolate1+chocolate2)
        if balance>=0:
            return balance
        return money