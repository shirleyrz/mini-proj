# Tests for Cache
#
# M<mayli.he@gmail.com> 2016

import unittest
from cache import LRUCache, MRUCache, LFUCache

class TestCache(unittest.TestCase):

    def test_lru(self):
        cache = LRUCache(10)
        cache.set("1", 1)
        cache.set("2", 2)
        cache.set("3", 3)
        self.assertEqual(cache.get("2"), 2)

        cache.set("4", 4)
        cache.set("5", 5)
        cache.set("6", 6)
        cache.set("7", 7)
        cache.set("8", 8)
        cache.set("9", 9)
        self.assertEqual(cache.get("8"), 8)

        cache.set("10", 10)
        cache.set("11", 11)
        self.assertEqual(cache.get("1"), None)
        self.assertEqual(cache.get("3"), 3)

    def test_mru(self):
        cache = MRUCache(5)
        cache.set("1", 1)
        cache.set("2", 2)
        cache.set("3", 3)
        self.assertEqual(cache.get("2"), 2)

        cache.set("4", 4)
        cache.set("5", 5)
        cache.set("6", 6)
        self.assertEqual(cache.get("2"), 2)

        cache.set("7", 7)
        self.assertEqual(cache.get("2"), None)

    def test_lfu(self):
        cache = LFUCache(3)
        cache.set("1", 1)
        cache.set("2", 2)
        cache.set("3", 3)
        self.assertEqual(cache.get("2"), 2)

        cache.set("4", 4)
        self.assertEqual(cache.get("1"), None)
        self.assertEqual(cache.get("2"), 2)

        cache.set("5", 5)
        cache.set("6", 6)
        self.assertEqual(cache.get("4"), None)
        self.assertEqual(cache.get("2"), 2)


if __name__ == '__main__':
    unittest.main()
