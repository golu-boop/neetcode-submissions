class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
                maxone = max(maxone,count)
            elif n == 0:
                count = 0
        return maxone