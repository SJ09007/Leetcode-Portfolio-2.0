class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max=max(nums)
        moves=0
        for num in nums:
            moves+=Max-num
        return moves        