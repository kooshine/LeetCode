# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def dfs(visited, i, j):
            if visited[i][j]:
                return 0
            if self.bigger(i, j, threshold):
                return 0
            if i > rows or j > cols or i < 0 or j < 0:
                return 0
            visited[i][j] = 1
            return 1 + dfs(visited, i+1,j) + dfs(visited, i-1, j) + dfs(visited, i, j+1) + dfs(visited, i, j-1)

        visited = [[0 for i in range(cols+1)] for j in range(rows+1)]
        print visited
        return dfs(visited, 0, 0)

    def bigger(self, i, j, threshold):
        total = 0
        while i > 0:
            total += (i % 10)
            i = i/10
        while j > 0:
            total += (j % 10)
            j = j / 10
        return True if total > threshold else False
if __name__ == "__main__":
    s = Solution()
    print s.movingCount(0, 3, 1)
