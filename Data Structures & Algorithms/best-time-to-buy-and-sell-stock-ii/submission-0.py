class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        max_profit = 0
        left = 0
        right = 1
        temp_pro = []
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                temp_pro.append(profit)
                left += 1
            else:
                left = right
            
            right += 1
        return sum(temp_pro)