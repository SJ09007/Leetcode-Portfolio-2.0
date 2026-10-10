class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff)<=k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2
            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                high = mid
            else:
                low = mid + 1

        x = low
        ans = 0
        used = 0

        for d in diff:
            if d > x:
                used += d - x
                d = x
            ans += d * d

        remaining = k - used

        for d in diff:
            if remaining == 0:
                break
            if d >= x and x > 0:
                ans -= 2 * x - 1
                remaining -= 1

        return ans