# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/4sum/


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        result = []
        if N < 4:
            return []
        nums.sort()

        a = 0
        while a < N-3:
            if a >= 1 and nums[a] in nums[:a]: #读过的跳过
                a += 1
                continue

            b = a + 1
            while b < N-2:
                print nums[a], nums[b]
                if nums[b] in nums[a+1: b]:     #读过的跳过
                    b += 1
                    continue
                start = b + 1
                end = N-1
                while start < end:
                    four = nums[a]+nums[b]+nums[start]+nums[end]
                    if four == target:
                        result.append([nums[a], nums[b], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                        while start < end and nums[end] == nums[end+1]:
                            end -= 1
                    elif four < target:
                        start += 1
                    else:
                        end -= 1
                b += 1
            a += 1

        return result

if __name__ == "__main__":
    s = Solution()
    print s.fourSum([1,0,-1,0,-2,2], 0)
    print s.fourSum([0,0,0,0], 0)
    print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)
