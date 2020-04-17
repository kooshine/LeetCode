# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        #return base ** exponent
        ret = 1
        if base == 0 or exponent == 1:
            return base
        if exponent == -1:
            return 1.0/base
        if exponent == 0:
            return 1
        tmp = abs(exponent)
        while tmp > 1:
            if tmp & 1 :
                ret = base
            ret *= (base * base)
            tmp = tmp >> 2

        return ret if exponent > 0 else 1.0/ret
