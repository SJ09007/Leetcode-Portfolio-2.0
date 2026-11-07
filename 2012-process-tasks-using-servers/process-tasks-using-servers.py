import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        ans = []
        time = 0

        for j, t in enumerate(tasks):
            time = max(time, j)

            # No free server: wait for the earliest one to finish
            if not free:
                time = max(time, busy[0][0])

            # Release all servers that are done by `time`
            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + t, w, i))

        return ans