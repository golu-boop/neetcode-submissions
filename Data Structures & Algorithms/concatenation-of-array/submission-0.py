class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        double = n*2
        ans = [0]*double

        for i in range(n):
            ans[i] = nums[i] # if we do nums[i%n]
            ans[i+n] = nums[i] # we don't need this line even

        return ans