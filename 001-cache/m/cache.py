# Simple LRUCache
# M<mayli.he@gmail.com> 2016

from collections import OrderedDict

class LRUCache(object):
    """ Simple LRUCache """
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = OrderedDict()

    def _update(self, key, value):
        del self._cache[key]
        self._cache[key] = value

    def set(self, key, value):
        if key in self._cache:
            self._update(key, value)
        if len(self._cache) >= self._capacity:
            # Pop out least recently used item.
            self._cache.popitem(last=False)
        self._cache[key] = value

    def get(self, key):
        if key in self._cache:
            self._update(key, self._cache[key])
        return self._cache.get(key)
