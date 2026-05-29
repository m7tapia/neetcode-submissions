class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        sell_index = 1
        max_profit = 0

        while sell_index < len(prices):
            buy_price = prices[buy_index]
            sell_price = prices[sell_index]

            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)

            if profit < 0:
                buy_index = sell_index

            sell_index += 1

        return max_profit

        #2 pointer approach -- we have two pointers start in the beginning. one for buy the other for sell.
        
        #if our profit comes out to be negative that means that we should move our buy_index forward to our sell_index b/c
        #we found a cheaper price to buy at. Doing this, our buy pointer will
        #always end up the cheapest price.
        
        #If our profit is positive or 0 we should move our sell pointer to see if there's any selling price
        #where we can get a higher profit.

        #Keep track of our max profit and end when our sell_pointer reaches the end

        #O(n) time complexity and O(1) space complexity