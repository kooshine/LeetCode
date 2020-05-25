# -*- coding: utf-8 -*-

import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = len(nums1), len(nums2)
        pos1, pos2 = (a+b)/2, (a+b)/2
        if (a + b) % 2 == 0:
            pos1, pos2 = (a+b)/2, (a+b)/2 - 1
        i, j = 0, 0
        pos, tmp = 0, 0
        ret = []
        while i < a and j < b:
            if nums1[i] < nums2[j]:
                tmp = nums1[i]
                i += 1
            else:
                tmp = nums2[j]
                j += 1
            if pos == pos2:
                ret.append(tmp)
            if pos == pos1:
                ret.append(tmp)
                break
            pos += 1
        while i < a:
            if pos == pos2:
                ret.append(nums1[i])
            if pos == pos1:
                ret.append(nums1[i])
                break
            pos += 1
            i += 1
        while j < b:
            if pos == pos2:
                ret.append(nums2[j])
            if pos == pos1:
                ret.append(nums2[j])
                break
            pos += 1
            j += 1
        return (ret[0] + ret[1]) / 2.0
        """
        news = []
        a, b = len(nums1), len(nums2)
        i, j = 0, 0
        while i < a and j < b:
            if nums1[i] < nums2[j]:
                news.append(nums1[i])
                i += 1
            else:
                news.append(nums2[j])
                j += 1
        if i < a:
            news.extend(nums1[i:])
        if j < b:
            news.extend(nums2[j:])
        print news
        a = len(news)
        if a % 2 == 0:
            return (news[a/2] + news[a/2 - 1]) / 2.0
        else:
            return float(news[a/2])
        """

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    nums1 = map(int, line.split())
    print nums1
    line = sys.stdin.readline().strip()
    nums2 = map(int, line.split())
    print nums2
    s = Solution()
    print s.findMedianSortedArrays(nums1, nums2)
