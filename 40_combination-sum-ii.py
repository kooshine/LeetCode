# -*- coding: utf-8 -*-
# https://leetcode-cn.com/problems/combination-sum-ii/


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(candidates)
        if N == 0:
            return []
        result = []
        candidates.sort()

        def dfs(start, size, path, target):
            if target < 0:
                return
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, size):
                if i > start and candidates[i] == candidates[i-1]:  #去重
                    continue
                path.append(candidates[i])
                dfs(i+1, size, path, target-candidates[i])
                print path
                path.pop()

        dfs(0, N, [], target)
        return result

if __name__ == "__main__":
    s = Solution()
    #print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([2,5,2,1,2], 5)
