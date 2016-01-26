package cache;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Least Recently User（LRU）
 * 
 * @author rong
 *
 */
public class LRU {

	// Store key-value pair for cache
	private HashMap<String, Object> cache;
	// Store the order of the key
	private Queue<String> queue;
	// length of the cache
	private int length = 10;

	public LRU() {
		cache = new HashMap<String, Object>();
		queue = new LinkedList<String>();
	}

	public void insert(String key, Object value) {
		if (queue.size() < length) {
			if (cache.containsKey(key)) {
				queue.remove(key);
			}
			cache.put(key, value);
			queue.add(key);
		} else {
			String oldKey = queue.remove();
			cache.remove(oldKey);
			cache.put(key, value);
		}
		print("Insert : " + key + "=" + value + "; queue=" + queue.toString());
	}

	public Object lookup(String key) {
		Object rs = null;
		if (cache.containsKey(key)) {
			queue.remove(key);
			queue.add(key);
			rs = cache.get(key);
		}

		print("Look up : " + key + ", get " + rs + "; queue=" + queue.toString());
		return rs;
	}

	/*
	 * TEST Cases
	 */

	public static void main(String[] args) {
		LRU cache = new LRU();
		cache.insert("1", 1);
		cache.insert("2", 2);
		cache.insert("3", 3);
		cache.lookup("2");
		cache.insert("4", 4);
		cache.insert("5", 5);
		cache.insert("6", 6);
		cache.insert("7", 7);
		cache.insert("8", 8);
		cache.insert("9", 9);
		cache.lookup("8");
		cache.insert("10", 10);
		cache.insert("11", 11);
		cache.lookup("1");
		cache.lookup("3");

	}

	static void print(String str) {
		System.out.println(str);
	}
}
