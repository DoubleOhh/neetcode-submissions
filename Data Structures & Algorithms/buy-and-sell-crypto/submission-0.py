class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = prices[0]
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > profit:
                profit = price - minprice
        return profit

            