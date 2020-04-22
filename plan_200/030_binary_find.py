# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        start, end = 0, len(data)-1
        while start <= end:
            mid = (start+end)//2
            if k >= data[mid]:
                start = mid + 1
            else:
                end = mid - 1
        right = start
        start, end = 0, len(data)-1
        while start <= end:
            mid = (start + end) // 2
            if k <= data[mid]:
                end = mid - 1
            else:
                start = mid + 1
        left = end
        return right - left - 1
        """
        times = 0
        start,end= 0, len(data)
        mid = (start+end)/2

        while start < end:
            mid = (start+end)/2
            if k > data[mid]:
                start = mid + 1
            elif k < data[mid]:
                end = mid - 1
            else:
                times += 1
                break
        for i in range(mid+1, end):
            if data[i] != k:
                break
            times += 1
        for i in range(mid-1, start-1, -1):
            if data[i] != k:
                break
            times += 1
        return times
        """
