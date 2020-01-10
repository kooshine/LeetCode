# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/sudoku-solver/

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
        print row,'\n', col,'\n', block

        empty_pos = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty_pos.append((i,j))
                #self.place_num(board, i, j, empty_pos)


        def dfs(start):
            if start == len(empty_pos):
                return True
            i, j = empty_pos[start]
            b = (i // 3)*3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(start+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        dfs(0)
        return board

    def place_num(self, board, row, col, empty_pos):
        one = self.rows(row, board)
        two = self.cols(col, board)
        three = self.little_board(row, col, board)
        exist = one + two + three
        exist = list(set(exist))
        possible_answer = []
        for i in range(1, 10):
            if str(i) not in exist:
                possible_answer.append(str(i))
        N = len(possible_answer)
        if N == 1:
            board[row][col] = possible_answer[0]
        else:
            empty_pos.append((row, col))


    def rows(self, row, board):
        result = []
        for i in range(9):
            if board[row][i] != ".":
                result.append(board[row][i])

        return result

    def cols(self, col, board):
        result = []
        for i in range(9):
            if board[i][col] != ".":
                result.append(board[i][col])
        return result

    def little_board(self, row, col, board):
        tmp = board[row][col]
        result = []
        row = row / 3
        col = col / 3
        for i in range(3*row, 3*row+3):
            for j in range(3*col, 3*col+3):
                if board[i][j] != ".":
                    result.append(board[i][j])
        return result


if __name__ == "__main__":
    s = Solution()
    """
    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    """
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    print s.solveSudoku(board)

"""
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
"""


