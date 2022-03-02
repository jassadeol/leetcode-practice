class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        
        buy = prices[0]
        for price in prices:
            buy = min(buy, price)
            if ((price - buy) > maxPro):
                maxPro = price - buy
        return maxPro
