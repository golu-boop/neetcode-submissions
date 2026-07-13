class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for fq in freq.values():
            if fq > 1:
                return True
        
        return False