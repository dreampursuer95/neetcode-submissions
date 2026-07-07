class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = dict()
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in self.mem:
                return self.mem[amount]

            min_count = float('inf')
            for coin in coins:
                if amount >= coin:
                    res = dfs(amount - coin)
                    if res != -1:
                        min_count = min(min_count, res + 1)
            self.mem[amount] = -1 if min_count == float('inf') else min_count
            return self.mem[amount]
        return dfs(amount)
