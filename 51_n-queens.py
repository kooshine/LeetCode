# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        """
        tmp = ""
        for i in range(n):
            tmp += "."
        path = [ tmp for j in range(n)]
        """
        path = [["." for i in range(n)] for j in range(n)]

        self.dfs(result, path, 0, n)

        return result

    def could_palce(self, row, col, path):
        if "Q" in path[row][:]:
            return False
        for i in range(len(path)):
            if "Q" == path[i][col]:
                return False
        main = row + col
        sub_main = row-col
        for i in range(len(path)):
            for j in range(len(path)):
                if i + j == row+col and "Q" == path[i][j]:
                    return False
                if i - j == row - col and "Q" == path[i][j]:
                    return False
        return True

    def dfs(self, result, path, row, n):
        if row == n:
            """
            from copy import deepcopy
            tmp = deepcopy(path)
            """
            tmp = []
            for i in range(len(path)):
                tmp.append("".join(path[i]))
            result.append(tmp)
            return

        for col in range(n):
            if self.could_palce(row,col, path):
                path[row][col] = "Q"
                self.dfs(result,path, row+1, n)
                path[row][col] = "."

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(4)
