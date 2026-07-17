import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:]
            temp.pop(i)
            prod = math.prod(temp)
            res.append(prod)

        return res