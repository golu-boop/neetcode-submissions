class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = rows * cols - 1

        while r <= c:
            mid = (r + c) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                r = mid + 1
            else:
                c = mid - 1

        return False