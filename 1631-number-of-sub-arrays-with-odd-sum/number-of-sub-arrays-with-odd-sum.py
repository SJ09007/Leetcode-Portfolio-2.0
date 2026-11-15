class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0      # count of prefix sums by parity (empty prefix = 0 is even)
        prefix = 0
        ans = 0
        for x in arr:
            prefix += x
            if prefix % 2:    # current prefix odd -> pair with earlier even prefixes
                ans += even
                odd += 1
            else:             # current prefix even -> pair with earlier odd prefixes
                ans += odd
                even += 1
        return ans % MOD