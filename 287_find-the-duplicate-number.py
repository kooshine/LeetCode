# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/find-the-duplicate-number/
#same as No.169

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        statis = dict()
        n = len(nums)

        for i in range(n):
            if statis.get(nums[i]):
                statis[nums[i]] += 1
            else:
                statis.update({nums[i]: 1})

        for k, v in statis.items():
            if v >= 2:
                return k
if __name__ == "__main__":
    s = Solution()
    print s.findDuplicate([1,3,4,2,2])
