# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """timeout
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                return True
        return False
        """
        hmap = dict()
        for i in range(len(nums)):
            if hmap.get(nums[i]) != None:
                hmap[nums[i]] += 1
            else:
                hmap.update({nums[i]: 1})

        return False if len(hmap) == len(nums) else True

if __name__ == "__main__":
    s = Solution()
    print s.containsDuplicate([1,2,3,1])
