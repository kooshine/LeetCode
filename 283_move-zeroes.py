# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 1
        for i in range(n):
            if nums[i] == 0:
                for j in range(start, n):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        start = j + 1
                        break
            else:
                start += 1
        return nums

if __name__ == "__main__":
    s = Solution()
    print s.moveZeroes([0,1,0,3,12])
