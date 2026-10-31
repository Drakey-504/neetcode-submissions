class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        total = len(matrix) * len(matrix[0])
        row_size = len(matrix[0])

        l, r = 0, total-1

        while l<=r:
            mid = l + (r-l)//2

            mid_num = matrix[mid//row_size][mid%row_size]

            if mid_num < target:
                l = mid + 1
            elif mid_num > target:
                r = mid - 1
            else:
                return True

        return False            
        