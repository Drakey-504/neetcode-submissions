class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        l , r = 0,0

        while r < len(prices): 

            res = max(res, prices[r] - prices[l])  

            if prices[r] < prices[l]:
                l = r
                r = r + 1
            else:
                r += 1   

        return res           