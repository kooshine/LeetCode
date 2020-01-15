# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """timeout
        def helper(i, j):
            if i == 0 or j == 0:
                return 1
            return helper(i-1, j) + helper(i, j-1)

        return helper(m-1, n-1)
        """
        dp = [[1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(7,3)
    print s.uniquePaths(23,12)

