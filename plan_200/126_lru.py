# -*- coding: utf-8 -*-
import sys

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        ret = -1
        flag = 0
        for index, value in enumerate(self.cache):
            if value[0] == key:
               print value[1]
               ret = value[1]
               flag = 1
               break

        if flag == 1:
            self.cache.pop(index)
            self.cache.append([key, ret])

        return ret

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        update_index = -1
        for index, item in enumerate(self.cache):
            if item[0] == key:
                update_index = index
                break

        if update_index != -1:
            self.cache.pop(update_index)
            self.cache.append([key,value])
        else:
            if len(self.cache) >= self.capacity:
                self.cache.pop(0)

            self.cache.append([key, value])

        print self.cache

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    capacity = int(sys.stdin.readline().strip())
    obj = LRUCache(capacity)
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        operations = sys.stdin.readline().strip().split(" ")
        if operations[0] == "put":
            key,value = int(operations[1]), int(operations[2])
            obj.put(key, value)
        if operations[0] == "get":
            key = int(operations[1])
            print obj.get(key)
