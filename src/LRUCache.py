__author__ = 'chifeng'

# https://leetcode.com/problems/lru-cache/
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) -
Get the value (will always be positive) of the key if the key exists in the
cache, otherwise return -1.

set(key, value) -
Set or insert the value if the key is not already present. When the cache
reached its capacity, it should invalidate the least recently used item before
inserting a new item.
'''

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        # self.oldest_key = None
        self.newest_key = None
        # {key: [val, older_key, newer_key]}
        # older_key == None if self.oldest_key == key
        self.dict = {}

    # @return an integer
    def get(self, key):
        lb_value, lb_older, lb_newer = 0, 1, 2
        record = self.dict.get(key)
        if None == record:
            return -1
        value = record[lb_value]
        if key == self.newest_key:
            return value
        self.detach(key)
        self.attach_as_newest(key, value)
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.capacity <= 0:
            return
        lb_value, lb_older, lb_newer = 0, 1, 2
        record = self.dict.get(key)
        if None != record:
            record[lb_value] = value
            if key == self.newest_key:
                return
            self.detach(key)
            self.attach_as_newest(key, value)
        else:
            if self.capacity == len(self.dict):
                oldest = self.dict[self.newest_key][lb_newer]
                self.detach(oldest)
            self.attach_as_newest(key, value)

    def detach(self, key):
        lb_value, lb_older, lb_newer = 0, 1, 2
        record = self.dict.get(key)
        assert(None != record)
        older = record[lb_older]
        newer = record[lb_newer]
        self.dict[older][lb_newer] = newer
        self.dict[newer][lb_older] = older
        #del(self.dict[key])
        self.dict.pop(key)

    def attach_as_newest(self, key, val):
        lb_value, lb_older, lb_newer = 0, 1, 2
        if 0 == len(self.dict):
            self.dict[key] = [val, key, key]
            self.newest_key = key
            return
        record = self.dict.get(key)
        assert(None == record)
        newest = self.newest_key
        oldest = self.dict[newest][lb_newer]
        self.dict[key] = [val, newest, oldest]
        self.dict[newest][lb_newer] = key
        self.dict[oldest][lb_older] = key
        self.newest_key = key

#cache = LRUCache(0)
cache = LRUCache(1)
cache.set(1, 10)
cache.set(1, 100)
print(cache.get(1))
cache.set(2, 20)
print(cache.get(1))

cache = LRUCache(3)
cache.set(1, 10)
cache.set(2, 20)
cache.set(3, 30)
print(cache.get(2))
cache.set(4, 40)
print(cache.get(1))
