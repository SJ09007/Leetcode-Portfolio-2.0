from collections import deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([1])
        ans = float('inf')

        while queue:
            node = queue.popleft()
            for nei, d in graph[node]:
                ans = min(ans, d)
                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)

        return ans