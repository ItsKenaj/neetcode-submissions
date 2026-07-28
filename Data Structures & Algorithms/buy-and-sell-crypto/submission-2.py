class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Best time to buy and sell stock:
        prices[i] is the price of the stock on the ith day

        return max profit one can achieve buy making a single buy and sell
        given the prices trajectory

        
        """
        n = len(prices)
        if n <= 1:
            return 0

        l, r = 0, 1
        max_profit = 0
        while r < n:
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
                
        return max_profit


