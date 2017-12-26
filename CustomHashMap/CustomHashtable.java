package custom.hashtable;

import lombok.Getter;

/**
 * Hashtable implementation similar to <code>java.util.HashMap</code> {@link java.util.HashMap}.
 * @author Suyash
 */
public class CustomHashtable<K, V> {
	/** 
	 * Each position in this array will represent a bucket, And this whole array will serve
	 * as a hashtable.
	 */
	private Node<K,V> table[];
	
	/**
	 * Total number of buckets available in this hashtable, which is equal to <code>table.length</code> 
	 */
	private Integer capacity;
	
	/**
	 * Total number of elements present in the hashtable at any moment.
	 */
	@Getter
	private Integer size;
	
    public CustomHashtable(Integer capacity){
		this.capacity = capacity;
		table = new Node[capacity];
		size = 0;
	}
	
	public V put(K key,V value){
		// Fetching the bucket(i.e. index) in which this element(key, value pair) needs to be stored.
		int index = getIndex(key);
		
		// Creating a new node.
		Node<K,V> newNode = new Node<K,V>(key, value, null);
		
		// Fetching the first element present(stored) in this bucket, if bucket is not empty. otherwise storedNode will be null.
		Node<K,V> storedNode = table[index];
		
		// If target bucket is empty, Just store this element as a first element in this bucket.
		if(storedNode == null){
			table[index] = newNode; 
		} else {	
			// If target bucket is not empty then iterate through all the elements in this bucket in order to check if the this is a duplicate element(key).
			for(Node<K,V> i=storedNode; i!=null; i=i.next){
				// If this is duplicate element(key), replace the older value with newer value for this key.
				if(i.key.equals(key)){
					V oldVal = i.value;
					i.value = value;
					size++;
					return oldVal;
				}
			}
			
			// If we came here, Which means that no such element was there and just insert this element as a first element in target bucket
			// in the form of linked list and adjust the link.
			table[index] = newNode;
			newNode.next = storedNode;
		}
		size++;
		return null;
	}
	
	public V get(K key){
		int index = getIndex(key);
		Node<K,V> storedNode = table[index];
		for(Node<K,V> i=storedNode; i!=null; i=i.next){
			if(i.key.equals(key)) return i.value;
		}
		return null;
	}
	
	public void remove(K key){
		// Fetching the bucket(i.e. index) in which the underlying element(key, value pair) is stored.
		int index = getIndex(key);
		
		// Fetching the first element present(stored) in this bucket, if bucket is not empty. otherwise storedNode will be null.
		Node<K,V> storedNode = table[index];
		
		if(storedNode!=null) {
			Node<K,V> prevStoredNode = null;
			
			// Iterate through all the elements in this bucket until we found the match, Or all the elements have been visited.
            while (storedNode.next != null && !storedNode.key.equals(key)) {
            	prevStoredNode = storedNode;
                storedNode = storedNode.next;
            }
            
            if (storedNode.key.equals(key)) {
            	
            	// If we found the match at the first position inside target bucket (Note-above while loop didn't run in this case.)
                if (prevStoredNode == null) {
                    table[index] = storedNode.next;
                } else {
                	prevStoredNode.next = storedNode.next;
                }
                size--;
            }
		}
	}
	
	@Override
	public String toString() {
		String str="";
		for(int i=0; i<table.length; i++){
			str = str+"\nBucket-"+i+" : ";
			for(Node<K,V> j=table[i]; j!=null; j=j.next){
				str = str + j.value+" ";
			}
		}
		return str;
	}
	
	/**
	 * 
	 * @param key
	 * @return bucket number corresponding to this key. Bucket number is calculated on the basis of hashcode of <code>key</code>.
	 */
	private int getIndex(K key){
		int hashCode = key.hashCode(); 
		int index = hashCode % capacity;
		return index;
	}
	
	/**
	 * An instance of this class represents a node/element.
	 * Elements are distinguished on the basis of their <code>key</code>. 
	 */
	static class Node<K, V>{
		final K key;
		V value;
		Node<K,V> next;
		
		Node(K key, V value, Node<K,V> next){
			this.key = key;
			this.value = value;
			this.next = next;
		}
	}
}
