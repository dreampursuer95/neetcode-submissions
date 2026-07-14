class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        curr = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            curr = min(curr, prices[i])
            if prices[i] > curr:
                max_diff = max(max_diff, prices[i] - curr)
            print(f"{i} {curr} {max_diff}")
        return max_diff
