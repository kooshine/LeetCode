# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        m = len(sequence)
        if m == 0:
            return False
        root = sequence[-1]
        i = 0
        for i in range(m):
            if sequence[i] > root:
                break
        for j in range(i, m-1):
            if sequence[j] < root:
                return False

        is_left, is_right = True, True
        print i
        if i > 0:
            print sequence[:i]
            is_left = self.VerifySquenceOfBST(sequence[:i])
        if i < m-1:
            print sequence[i:m-1]
            is_right = self.VerifySquenceOfBST(sequence[i:-1])
        return is_left and is_right

if __name__ == "__main__":
    s = Solution()
    print s.VerifySquenceOfBST([4,6,7,5])
