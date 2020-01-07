# -*- coding: utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in board[row][col+1:]:
                    return False
                if board[row][col] in self.cols(row, col, board):
                    return False
                if board[row][col] in self.little_board(row, col, board):
                    return False

        return True

    def cols(self, row, col, board):
        result = []
        for i in range(row+1, 9):
            result.append(board[i][col])
        return result


    def little_board(self, row, col, board):
        tmp = board[row][col]
        result = []
        row = row / 3
        col = col / 3
        for i in range(3*row, 3*row+3):
            for j in range(3*col, 3*col+3):
                result.append(board[i][j])
        result.remove(tmp)
        return result

if __name__ == "__main__":
    s = Solution()
    """
    sodu = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    """
    sodu =[
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
    print s.isValidSudoku(sodu)
