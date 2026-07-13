class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Candidate = None
        count = 0

        for num in nums:
            if count == 0:
                Candidate = num
            
            if num == Candidate:
                count += 1
            else:
                count -= 1

        return Candidate