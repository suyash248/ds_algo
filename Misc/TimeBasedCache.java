package general;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class TimeBasedCache {
	public static int CACHE_SIZE;
	public static long TTL;
	public static void main(String[] args) {
		Scanner scanner = null;
		try {
			System.out.println("Started at " + LocalDateTime.now());
			scanner = new Scanner(System.in);
			
			System.out.print("Enter cache size : ");
			CACHE_SIZE = scanner.nextInt();
			
			System.out.print("Enter TTL (in sec): ");
			TTL = scanner.nextLong();
			
			while(true) {
				
				String item = scanner.nextLine();
				if(!item.isEmpty()) {
					System.out.print("\nEnter key-value pair -> ");
					
					String pair[] = item.split(":");
					System.out.println("Inserting a key : "+pair[0]+" at " + LocalDateTime.now());
					CacheUtil.CACHE.put(pair[0], pair[1]);
				}
			}
		} catch (Exception e) {
			scanner.close();
			e.printStackTrace();
		}
		System.out.println(CacheUtil.CACHE.getCache());
	}
}

enum CacheUtil {
	CACHE;
	private ConcurrentMap<String, Entry> cache = new ConcurrentHashMap<>();
	private Object lock = new Object();
	
	CacheUtil() {
		ScheduledExecutorService scheduledExecutor = Executors.newScheduledThreadPool(2);
		scheduledExecutor.scheduleAtFixedRate(new ExpiryChecker(cache, lock), 0, 1, TimeUnit.SECONDS);
	}
	
	public void put(String key, Object value) {
		synchronized (lock) {
			if(cache.size()>=TimeBasedCache.CACHE_SIZE) {
				System.out.println("Cache is full.....Waiting for elements expiration.");
				try {
					System.out.println("Cache is full.....Waiting for elements expiration.");
					lock.wait();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			cache.put(key, new Entry(value, System.currentTimeMillis() + TimeBasedCache.TTL * 1000));
		}
	}
	
	public void get(String key) {
		cache.get(key);
	}
	
	public ConcurrentMap<String, Entry> getCache() {
		return cache;
	}
}

class Entry {
	private Object value;
	private Long ttl;
	
	public Entry(Object value, Long ttl) {
		super();
		this.setValue(value);
		this.setTtl(ttl);
	}

	public Object getValue() {
		return value;
	}

	public void setValue(Object value) {
		this.value = value;
	}

	public Long getTtl() {
		return ttl;
	}

	public void setTtl(Long ttl) {
		this.ttl = ttl;
	}
	
	@Override
	public String toString() {
		return value.toString() + " - " + ttl;
	}
}

class ExpiryChecker implements Runnable {
	private ConcurrentMap<String, Entry> cache = new ConcurrentHashMap<>();
	private Object lock;
	
	public ExpiryChecker(ConcurrentMap<String, Entry> cache, Object lock) {
		this.cache = cache;
		this.lock = lock;
	}

	@Override
	public void run() {
		Set<String> keysToBeRemoved = new HashSet<>();
		for(Map.Entry<String, Entry> entry : cache.entrySet()) {
			Entry etr = entry.getValue();
			if(etr.getTtl()<=System.currentTimeMillis()) {
				keysToBeRemoved.add(entry.getKey());
			}
		}
		
		for(String keyToBeRemoved : keysToBeRemoved) {
			System.out.println("\nRemoving key : " + keyToBeRemoved + " at " + LocalDateTime.now());
			cache.remove(keyToBeRemoved);
			synchronized(lock) {
				lock.notifyAll();
			}
		}
	}
	
}