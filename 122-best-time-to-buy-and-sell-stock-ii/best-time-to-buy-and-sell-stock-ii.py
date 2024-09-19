class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini=float('inf')
        count=0

        for price in prices:
            mini=min(mini,price)
            profit=price-mini
            count+=profit
            mini=price
        return count
        