# -*- coding: utf-8 -*-

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return []
        result = nums[:k]

        statics = dict()
        for item in nums:
            if item in statics:
                statics[item] += 1
            else:
                statics.update({item: 1})
        result = sorted(statics.items(),key=lambda item:item[1],reverse=True)
        tmp = [item[0] for item in result]
        return tmp[:k]

if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
