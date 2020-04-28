# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        def dfs(matrix,path, i, j, k):
            if not(i < rows and i >= 0) or not(j < cols and j >= 0) or not (matrix[i*cols + j] == path[k]):
                return False
            if k == len(path) - 1:
                return True
            #tmp, matrix[i][j] = matrix[i][j], "/"
            tmp = matrix[i*cols + j]
            matrix =  matrix[:i*cols+j] + "/" + matrix[i*cols+j+1:]
            res = dfs(matrix, path, i+1, j, k+1) or dfs(matrix, path, i, j+1, k+1) or dfs(matrix, path, i-1,j, k+1) or dfs(matrix, path,i, j-1, k+1)
            #matrix[i][j] = tmp
            matrix =  matrix[:i*cols+j] + tmp + matrix[i*cols+j+1:]
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(matrix, path,i, j, 0):
                    return True
        return False
if __name__ == "__main__":
    s = Solution()
    #matrix = [["a","b","c","e"], ["s", "f", "c","s"], ["a", "d", "e", "e"]]
    matrix = "ABCESFCSADEE"
    rows = 3
    cols = 4
    path = "ABCCED"
    print s.hasPath(matrix, rows, cols, path)
