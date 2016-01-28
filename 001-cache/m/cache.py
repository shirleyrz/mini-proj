# Cache Algorithms Playground
#
# M<mayli.he@gmail.com> 2016
# ref https://en.wikipedia.org/wiki/Cache_algorithms

from collections import OrderedDict, defaultdict
from itertools import count

class LRUCache(object):
    """ Least Recently Used (LRU) cache """
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


class MRUCache(LRUCache):
    """ Most Recently Used (MRU) cache """
    def set(self, key, value):
        if key in self._cache:
            self._update(key, value)
        if len(self._cache) >= self._capacity:
            # Pop out most recently used item.
            self._cache.popitem(last=True)
        self._cache[key] = value


class LFUCache(object):
    """ Least-Frequently Used (LFU) cache """
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}
        # Genereate uniq and sequential id to track recency.
        self._get_id = count()
        self._counter = defaultdict(lambda: (0, next(self._get_id)))

    def _remove(self, key):
        del self._cache[key]
        del self._counter[key]

    def _incr(self, key):
        c, id_ = self._counter[key]
        c += 1
        self._counter[key] = (c, id_)

    def set(self, key, value):
        is_new = True
        if key in self._cache:
            self._update(key, value)
            is_new = False
        if len(self._cache) >= self._capacity:
            # Pop out least frequently used item.
            _, victim_key = min([(c, k) for (k, c) in self._counter.items()])
            self._remove(victim_key)
        self._cache[key] = value
        if is_new:
            self._incr(key)

    def get(self, key):
        if key in self._cache:
            self._incr(key)
        return self._cache.get(key)
