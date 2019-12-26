# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        choose_list = [i for i in range(1, n+1)]
        size = n
        result = []
        self.dfs(choose_list, result, [], 0, size, k)
        return result

    def dfs(self, choose_list, result, path, start, size, k):
        #退出条件, k是遍历深度
        if len(path) == k:
            result.append(path[:])
            return

        for index in range(start, size):
            path.append(choose_list[index])
            self.dfs(choose_list, result, path, index+1, size, k)
            path.pop()      ##回溯
if __name__ == "__main__":
    s = Solution()
    print s.combine(4,2)
