# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        col = len(matrix[0])
        result = []
        row_start, col_start = 0, 0
        row_end, col_end = row-1, col-1

        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end+1):
                result.append(matrix[row_start][i])
                print "first", result
            row_start += 1
            for i in range(row_start, row_end+1):
                result.append(matrix[i][col_end])
                print "second", result
            col_end -= 1
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
                print "third", result
            if col_start <= col_end:
                for i in range(row_end, row_start-1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1
                print "forth", result
        return result

if __name__ == "__main__":
    s = Solution()
    matrix = [[1],[2],[3],[4],[5]]
    print s.printMatrix(matrix)
    matrix = [[1,2,3,4,5],[6,7, 8, 9, 10], [11,12,13,14,15], [16,17,18,19,20],[21,22,23,24,25]]
    print s.printMatrix(matrix)
    matrix = [[1]]
    #matrix = [[1,2],[3,4],[5,6],[7,8],[9,10]]
    print s.printMatrix(matrix)
