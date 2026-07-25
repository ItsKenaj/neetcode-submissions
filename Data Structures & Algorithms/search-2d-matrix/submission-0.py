class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        total = m * n
        l, r = 0, total - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // n
            idx = mid - (row * n)
            if matrix[row][idx] == target:
                return True
            elif matrix[row][idx] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return False
            