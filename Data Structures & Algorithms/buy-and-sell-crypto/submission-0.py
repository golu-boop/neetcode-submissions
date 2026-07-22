class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        max_profit = 0  
        for i in range(n):
            temp_max = 0
            for j in range(i,n):
                val = prices[j] - prices[i]
                if temp_max <= val:
                    temp_max = val

            max_profit = max(temp_max, max_profit)

        return max_profit