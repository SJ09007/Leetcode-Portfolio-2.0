class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        cnt, ans, l, r = Counter(), [0] * len(queries), 0, 0
        for q, i in sorted((q, i) for i, q in enumerate(queries)):
            while r < len(logs) and logs[r][1] <= q:
                cnt[logs[r][0]] += 1
                r += 1
            while l < r and logs[l][1] < q - x:
                s = logs[l][0]
                cnt[s] -= 1
                if not cnt[s]:
                    del cnt[s]
                l += 1
            ans[i] = n - len(cnt)
        return ans