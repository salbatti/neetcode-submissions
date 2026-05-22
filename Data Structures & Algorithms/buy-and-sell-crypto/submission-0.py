class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        max_diff=0
        while r < len(prices):
            if prices[r] < prices[l]:
                l=r
                r+=1
            else:
                diff = prices[r]-prices[l]
                max_diff=max(diff,max_diff)
                r+=1

        return max_diff



        