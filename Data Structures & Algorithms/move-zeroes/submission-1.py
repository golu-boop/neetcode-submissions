class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # FIX: Correctly cross-assign the values to swap them
                nums[insert_position], nums[i] = nums[i], nums[insert_position]
                
                insert_position += 1
