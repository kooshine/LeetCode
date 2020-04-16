# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        start = 0
        end = len(rotateArray)-1
        while start < end-1:
            mid = (start+end)/2
            if rotateArray[mid] > rotateArray[end]:
                start = mid
            if rotateArray[mid] < rotateArray[start]:
                end = mid
        return rotateArray[start] if rotateArray[start] < rotateArray[end] else rotateArray[end]
