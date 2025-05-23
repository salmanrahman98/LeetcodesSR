# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        maxPrice = prices[len(prices) - 1]
        for i in range(len(prices)-1, -1, -1):
            diff = maxPrice - prices[i]

            if diff > maxProfit:
                maxProfit = diff

            if prices[i] > maxPrice:
                maxPrice = prices[i]

        return maxProfit

    # nums = [2, 4, 1]
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))
