# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.dfs(nums, path, result)
        return result       ###打印出来所有路径

    def dfs(self, nums, path, result):
        if path is not []:###打印出来所有路径
            result.append(path[:])###打印出来所有路径
            #no return  全部遍历

        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[i+1:], path, result)
            path.pop()

        """
        result = [[]]
        for i in nums:
            for item in result:
                result = result + [item+[i]]
        return result
        """

        """
        超出内存限制
        result = [[],]
        for i in nums:
            for item in result:
                result.append(item+[i])
        return result
        """
        """
        (1)  [1,2]   时间超出限制
        result = [[],]
        index = 0
        size = len(nums)
        self.dfs(result, nums, index, size)
        return result

    def dfs(self, result, nums, index, size):
        if index == size-1:
            result.append(nums)
            return

        for item in result:
            result.append(item)
            item.append(nums[index])
            result.append(item)

        self.dfs(result, nums, index+1, size)
        """

if __name__ == "__main__":
    s = Solution()
    print s.subsets([1,2,3])
