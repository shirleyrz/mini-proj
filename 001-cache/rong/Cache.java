package cache;

public interface Cache<K, V> {
	
	private int capacity;

	public V get(K key);

	public void set(K key, V value);

}
