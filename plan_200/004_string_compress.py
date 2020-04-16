# -*- coding: utf-8 -*-

class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 0:
            return S
        alpha = [S[0]]
        nums = [1]
        j = 0
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                nums[j] += 1
            else:
                j += 1
                nums.append(1)
                alpha.append(S[i])
        if len(nums) * 2 >= len(S):
            return S
        else:
            S = ""
            for i in range(len(nums)):
                S += alpha[i] + str(nums[i])
            return S
