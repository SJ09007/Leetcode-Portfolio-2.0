from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            best = INF
            for k in (1, 2, 3):
                i = j - k
                if i >= 0:
                    best = min(best, dp[i] + k * k)
            dp[j] = best + costs[j - 1]
        return dp[n]