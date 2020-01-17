# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/generate-parentheses/


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        作减法 作加法
        """
        result = []

        def dfs(left, right, cur):
            if left == right == n:
                result.append(cur)
                return
            if right > left:
                return
            if left <= n:
                dfs(left +1, right, cur+"(")

            if right <= n:
                dfs(left, right+1, cur + ")")

        dfs(0, 0, "")
        return result

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)
