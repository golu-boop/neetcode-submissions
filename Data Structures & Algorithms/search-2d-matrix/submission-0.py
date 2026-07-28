class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for ro in range(rows):
            l = 0
            r = cols-1

            while l <= r:
                mid = (l + r)//2

                if matrix[ro][mid] == target:
                    return True
                
                if matrix[ro][mid] < target:
                    l = mid + 1
                elif matrix[ro][mid] > target:
                    r = mid - 1

                
        return False