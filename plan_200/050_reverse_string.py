# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        result = ""
        start = len(s)-1
        end = start
        while start >= 0:
            while s[end] != " " and end != 0:
                end -= 1
            if end == 0:
                tmp = s[end: start+1]
            else:
                tmp = s[end+1: start+1]
                tmp += " "
            result += tmp
            start = end -1
            end = start
        return result

if __name__ == "__main__":
    s = Solution()
    print s.ReverseSentence("I am a student.")
