class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        treating it as flattened 1d array, 
        since it is still 2d matrix, we'd need to carefully calculate
        row, col = divmod(mid, len(matrix[0]))
        """
        left = 0
        right = len(matrix)*len(matrix[0])-1

        while left<=right:
            mid = (left+right)//2

            row, col = divmod(mid, len(matrix[0]))

            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                right = mid-1
            else:
                left = mid+1
        return False   