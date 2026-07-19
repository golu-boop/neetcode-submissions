class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0:1}

        for num in nums:
            curSum = curSum + num
            diff = curSum - k

            if diff in prefixSums.keys():
                res += prefixSums[diff]

            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return res