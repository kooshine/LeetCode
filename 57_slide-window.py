# -*- coding: utf-8 -*-

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums = [i for i in range(1, target+1)]

        start = 0
        end = 1
        for i in range(1, target):
            if end >= target:
                break
            tmp = sum(nums[start: end+1])
            if tmp < target:
                end += 1
            elif tmp > target:
                start += 1
            else:
                result.append(nums[start:end+1])
                start += 1
                end += 1
        return result
