class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [x**2 for x in sorted(nums, key=abs)]