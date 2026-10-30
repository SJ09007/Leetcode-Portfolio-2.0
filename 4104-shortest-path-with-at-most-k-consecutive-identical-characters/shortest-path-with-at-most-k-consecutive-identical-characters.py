import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        INF = float('inf')
        dist = [INF] * (n * K)

        start = 0 *K +1
        dist[start] = 0
        heap = [(0, 0, 1)]  # (distance, node, run)

        while heap:
            d, u, r = heapq.heappop(heap)
            if d > dist[u * K + r]:
                continue
            if u == n - 1:
                return d  # first time the target is popped is the minimum
            lu = labels[u]
            for v, w in adj[u]:
                if labels[v] == lu:
                    nr = r + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                idx = v * K + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(heap, (nd, v, nr))

        return -1