# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/unique-paths-ii/
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = 0
        m = len(obstacleGrid)
        if m >= 0:
            n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        #dp = [[0]*n for _ in range(m)]
        obstacleGrid[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i-1] == 1 and obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0

        for i in range(1, m):
            if obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0


        #print dp
        return obstacleGrid[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    data = [
    [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    data = [[0]]
    data = [
        [0,1,0,0,0],
        [1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    print s.uniquePathsWithObstacles(data)

