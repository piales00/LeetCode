class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        menor = prices[0]
        resta = 0
        for i in range(0, len(prices)):
            if (menor > prices[i]):
                menor = prices[i]

            else if (resta < prices[i] - menor):
                resta = prices[i] - menor

        return resta 
        
