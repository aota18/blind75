# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit=0

        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[i] - prices[j] < 0:
                    maxProfit=max(maxProfit, abs(prices[i]-prices[j]))
        return maxProfit