class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        maxF = max(f for f, _ in items)
        minP = min(p for _, p in items)
        freq = [0] * (maxF + 1)
        for f, _ in items:
            freq[f] += 1
        mult = [0] * (maxF + 1)
        for d in range(1, maxF + 1):
            for k in range(d, maxF + 1, d):
                mult[d] += freq[k]
        dp = [0] * (budget + 1)
        for f, p in items:
            val = mult[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + val > dp[b]:
                    dp[b] = dp[b - p] + val
        ans = 0
        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget - b) // minP)
        return ans