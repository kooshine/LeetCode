# -*- coding: utf-8 -*-

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #return s.replace(" ", "%20")
        nums = 0
        for i in range(len(s)):
            if s[i] == " ":
                nums += 1

        nums = nums * 2 + len(s)

        ret = ["0" for i in range(nums)]
        print ret, nums
        j = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                print s[i], nums-j
                ret[nums-j] = s[i]
                j += 1
            else:
                ret[nums-j] = "0"
                ret[nums-j-1] = "2"
                ret[nums-j-2] = "%"
                j += 3

        print ret
        return "".join(ret)

if __name__ == "__main__":
    s = Solution()
    print s.replaceSpace("hello world")
