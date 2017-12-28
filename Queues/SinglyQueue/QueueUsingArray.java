package queue.array;

import lombok.Getter;

public class QueueUsingArray {
	@Getter
	private int capacity;
	@Getter
	private int size;
	
	private int front=-1,rear=-1;
	private Integer q[];
	
	public QueueUsingArray(int capacity) {
		this.capacity = capacity;
		q = new Integer[capacity];
	}
	
	public void insert(Integer elt) {
		if(isFull()) {
			throw new RuntimeException("Queue is full.");
		} else {
			if(isEmpty()) {
				front = (front+1) % capacity;
			} 
			rear = (rear+1) % capacity;
			q[rear] = elt;
			size++;
		}
	}
	
	public Integer delete() {
		if(isEmpty()) {
			throw new RuntimeException("Queue is empty.");
		} else {
			Integer frontItem = getFrontItem();		// Fetching item present at front, This is the item to be deleted.
			if(size==1) {
				rear=-1;
			} else {
				front = (front+1) % capacity;
			}
			size--;
			return frontItem;
		}
	}
	
	public Integer getFrontItem() {
		if(!isEmpty()) return q[front];
		return null;
	}
	
	public Integer getRearItem() {
		if(!isEmpty()) return q[rear];
		return null;
	}
	
	public boolean isFull() {
		if(size==capacity) return true;
		return false;
	}
	
	public boolean isEmpty() {
		if(size==0 && front<0 && rear<0) return true;
		return false;
	}
	
	@Override
	public String toString() {
		String res="";
		for(int i=0, j=front; i<size; j=(j+1)%capacity, i++) {
			res = res + q[j]+" ";
		}
		return res;
	}
}
