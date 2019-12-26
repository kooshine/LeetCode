# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(candidates)
        if size == 0:
            return []

        result = []
        self.dfs(candidates, [], result, 0, size, target)
        return result

    def dfs(self, candidates, path, result, start, size, target):
        if target < 0 :
            return
        if target == 0:
            result.append(path[:])
            return
        for index in range(start, size):
            path.append(candidates[index])
            self.dfs(candidates, path, result, index, size, target-candidates[index])
            path.pop()
        """
        size = len(candidates)
        if size == 0:
            return []

        result = []
        self.__dfs(candidates, [], target, 0, size, result)
        return result

    def __dfs(self, candidates, path, target, index, size, result):
        if target < 0:
            return
        if target == 0:
            result.append(path[:])
            return

        for i in range(index, size):
            path.append(candidates[i])
            #self.__dfs(candidates, path, target-candidates[i], index, size, result)
            self.__dfs(candidates, path, target-candidates[i], i, size, result)
            path.pop()
        """
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
