class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        max_profit = 0

        while buy_index < len(prices) and sell_index < len(prices):
            buy_price = prices[buy_index]
            sell_price = prices[sell_index]

            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)

            if profit < 0:
                buy_index += 1

            else:
                sell_index += 1

        return max_profit