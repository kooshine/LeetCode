# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        result = []
        nums.sort()
        if N < 3:
            return []
        index = 0
        while index < N-2:
            start = index + 1
            end = N - 1
            if index >= 1 and nums[index] in nums[:index]:
                index += 1
                continue
            while start < end:
                three = nums[index] + nums[start] + nums[end]
                if three == 0:
                    result.append([nums[index], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif three < 0:
                    start += 1
                else:
                    end -= 1
            index += 1

        return result
if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    print s.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])
