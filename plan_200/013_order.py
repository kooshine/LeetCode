# -*- coding: utf-8 -*-

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        """
        length = len(array)
        for i in range(length):
            for j in range(length-1, i, -1):
                if array[j]%2 == 1 and array[j-1]%2 == 0:
                    array[j], array[j-1] = array[j-1], array[j]
        return array
        """
        length = len(array)
        for i in range(length):
            if array[i] % 2 == 0:
                tmp = array[i]
                for j in range(i+1, length):
                    if array[j] % 2 == 1:
                        array[i] = array[j]
                        for k in range(j, i, -1):
                            array[k] = array[k-1]
                        array[i+1] = tmp
                        break
        return array
        """
        odd = []
        even = []
        for item in array:
            if item & 1:
                odd.append(item)
            else:
                even.append(item)
        return odd + even
        """
if __name__ == "__main__":
    s = Solution()
    print s.reOrderArray([1,2,3,4,5,6,7])
