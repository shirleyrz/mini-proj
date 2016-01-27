package cache;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Least Recently Used（LRU）
 * 
 * @author rong
 * @param <V>
 *
 */
public class LRUCache<K, V> implements Cache<K, V> {

	// Store key-value pair for cache
	private HashMap<K, V> cache;
	// Store the order of the key
	private Queue<K> queue;
	// length of the cache
	private int capacity;

	public LRUCache(int capacity) {
		this.capacity = capacity;
		this.cache = new HashMap<K, V>();
		this.queue = new LinkedList<K>();
	}

	@Override
	public void set(K key, V value) {
		if (queue.size() < capacity) {
			if (cache.containsKey(key)) {
				queue.remove(key);
			}
			cache.put(key, value);
			queue.add(key);
		} else {
			K oldKey = queue.remove();
			cache.remove(oldKey);
			cache.put(key, value);
		}
		System.out.println("Set : " + key + "=" + value + "; queue="
				+ queue.toString());
	}

	@Override
	public V get(K key) {
		V rs = null;
		if (cache.containsKey(key)) {
			queue.remove(key);
			queue.add(key);
			rs = cache.get(key);
		}

		System.out.println("Get : " + key + ", get " + rs + "; queue="
				+ queue.toString());
		return rs;
	}

}
