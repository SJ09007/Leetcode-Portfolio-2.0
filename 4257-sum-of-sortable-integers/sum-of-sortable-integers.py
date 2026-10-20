class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        a=nums
        # nxt[i] = smallest j >= i with a[j] > a[j+1] (j < n-1), else n
        nxt = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            if i < n - 1 and a[i] > a[i + 1]:
                nxt[i]=i
            else:
                nxt[i] =nxt[i+1]

        total = 0
        for k in range(1, n + 1):
            if n % k:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                j = nxt[s]
                if j < e:  # internal descent at j
                    # must be only one internal descent, and wrap must be fine
                    if nxt[j + 1] < e or a[e] > a[s]:
                        ok = False
                        break
                    lo, hi = a[j + 1], a[j]
                else:
                    lo, hi = a[s], a[e]
                if lo < prev_max:
                    ok = False
                    break
                prev_max = hi
            if ok:
                total += k
        return total