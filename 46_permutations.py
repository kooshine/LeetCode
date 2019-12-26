# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/permutations/submissions/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size == 0:
            return []
        result = []
        path = []
        self.dfs(nums, result, path)
        return result

    def dfs(self, nums, result, path):
        if nums == []:
            result.append(path[:])
            return

        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i+1:], result, path)
            path.pop()


if __name__ == "__main__":
    s = Solution()
    print s.permute([1,2,3])
