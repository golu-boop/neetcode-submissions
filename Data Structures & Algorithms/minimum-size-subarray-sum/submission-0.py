class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlen = float('inf')
        l = 0
        curr_sum = 0
        for r in range(n):
            curr_sum += nums[r]

            while curr_sum >= target:
                minlen = min(minlen, r - l + 1)
                curr_sum -= nums[l]
                l += 1

            
        return 0 if minlen == float('inf') else minlen