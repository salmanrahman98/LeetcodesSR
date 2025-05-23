# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(prices):
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[l] <= prices[r]:
                if maxProfit < prices[r] - prices[l]:
                    maxProfit = prices[r] - prices[l]
            r = r + 1

        return maxProfit

    # nums = [2, 4, 1]
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))
