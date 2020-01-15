# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
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
            if v >= n/2 + 1:
                return k
if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([2,2,1,1,1,2,2])
