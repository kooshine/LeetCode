# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """ timeout
        start = 0
        end = 0
        for i in range(len(nums)):
            if i > k:
                start = i - k
            end = i + k + 1
            if end >= len(nums):
                end = len(nums)

            tmp = nums[start:end]
            tmp.remove(nums[i])
            if nums[i] in tmp:
                return True

        return False
        """
        tmp = dict()

        for i,v in enumerate(nums):
            if tmp.get(v) != None and i-tmp.get(v) <= k:
                return True
            else:
                tmp[v] = i

        return False
        """
        if len(nums) <= 1:
            return False
        hmap = dict()
        start = 0
        end = k
        if end >= len(nums):
            end = len(nums)
        for i in range(start, end):
            if hmap.get(nums[i]) != None:
                hmap[nums[i]] += 1
            else:
                hmap.update({nums[i]: 1})


        for i in range(len(nums)):
            if i <= k:
                start = 0
            else:
                hmap = self.remove_map(nums[start], hmap)
                start += 1

            if i >= len(nums)  - k:
                end =  len(nums)
            else:
                self.add_map(nums[end], hmap)
                end += 1
            if hmap.get(nums[i]) > 1:
                return True

        return False

    def add_map(self, value, hmap):
        print hmap.get(value)
        if hmap.get(value) != None:
            hmap[value] += 1
        else:
            hmap.update({value: 1})

    def remove_map(self, value, hmap):
        if hmap.get(value) == 1:
            hmap.pop(value)
        else:
            hmap[value] -= 1
        return hmap
    """


if __name__ == "__main__":
    s = Solution()
    print s.containsNearbyDuplicate([1,2,3,1], k = 3)
    print s.containsNearbyDuplicate([1,0,1,1], k = 1)
    print s.containsNearbyDuplicate([1,2,3,1,2,3], k = 2)
    print s.containsNearbyDuplicate([1,1], k = 2)
