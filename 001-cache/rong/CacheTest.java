package cache;

public class CacheTest {

	
	/*
	 * TEST Cases
	 */

	public static void main(String[] args) {
		LRUCache<String, Integer> cache = new LRUCache<String, Integer>(10);
		cache.set("1", 1);
		cache.set("2", 2);
		cache.set("3", 3);
		cache.get("2");
		cache.set("4", 4);
		cache.set("5", 5);
		cache.set("6", 6);
		cache.set("7", 7);
		cache.set("8", 8);
		cache.set("9", 9);
		cache.get("8");
		cache.set("10", 10);
		cache.set("11", 11);
		cache.get("1");
		cache.get("3");
	}
}
