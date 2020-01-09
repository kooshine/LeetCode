# -*- coding: utf-8 -*-
#https://leetcode-cn.com/problems/candy/

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        if N == 0:
            return 0
        if N == 1:
            return 1

        total = [1 for item in ratings]


        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                total[i] = total[i-1]+1


        for i in range(N-2, 0, -1):
            if ratings[i] > ratings[i+1] and total[i] <= total[i+1]:
                total[i] = total[i+1]+1
        if ratings[0] > ratings[1]:
            total[0] = total[1] + 1

        if ratings[-1] > ratings[-2]:
            total[-1] = total[-2] + 1
        print total
        return sum(total)



if __name__ == "__main__":
    s = Solution()
    print s.candy([1,0,2])
    print s.candy([1,2,2])
    print s.candy([1,2,87,87, 87,2, 1])
    print s.candy([1,3,4,5,2])
    print s.candy([3,2,1,1,4,3,3])
