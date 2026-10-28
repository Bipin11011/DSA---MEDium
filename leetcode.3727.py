from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums1 = [abs(x) for x in nums]
        nums1.sort()

        n = len(nums1)
        total = 0
        take = 0
        m = n // 2

        for i in range(n):
            total += nums1[i] * nums1[i]

        for i in range(m):
            take += nums1[i] * nums1[i]

        return total - 2 * take
