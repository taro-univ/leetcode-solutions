class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #行列はm行n列ある
        #問題設定から, まず各行の先頭(matrix[i][0])と末尾(matrix[i][n])とtargetを比較し、行を特定
        #特定したk行の中で、列を特定すればよい(matrix[k][j]で, jについてbinary search)

        #行のサーチ
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        n = cols - 1
        d, u = 0, rows - 1
        m = 0

        while d <= u:
            m = d + ((u - d) // 2)
            if matrix[m][0] <= target and target <= matrix[m][n]:
                break
            elif target < matrix[m][0]:
                u = m - 1
            elif matrix[m][n] < target:
                d = m + 1

        #mが行数
        l, r = 0, cols - 1
        while l <= r:
            k = l + ((r - l) // 2)
            if target > matrix[m][k]:
                l = k + 1
            elif target < matrix[m][k]:
                r = k - 1
            else:
                return True

        return False