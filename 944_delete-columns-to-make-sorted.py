# -*- coding: utf-8 -*-

#https://leetcode-cn.com/problems/delete-columns-to-make-sorted/

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        if A == []:
            return 0
        size = len(A[0])

        for i in range(size):
            tmp = [A[j][i] for j in range(len(A))]
            print tmp
            for j in range(1, len(tmp)):
                if tmp[j] < tmp[j-1]:
                    result += 1
                    break

        return result

if __name__ == "__main__":
    s = Solution()

    #print s.minDeletionSize(["cba", "daf", "ghi"])
    print s.minDeletionSize(["zyx", "wvu", "tsr"])
