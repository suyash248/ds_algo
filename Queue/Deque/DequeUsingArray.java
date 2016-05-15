package deque.array;

import lombok.Getter;

public class DequeUsingArray {
	@Getter
	private int capacity;
	@Getter
	private int size;
	
	private int front=-1,rear=-1;
	private Integer q[];
	
	public DequeUsingArray(int capacity) {
		this.capacity = capacity;
		q = new Integer[capacity];
	}
	
	public void insertAtRear(Integer elt) {
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
	
	public Integer deleteFromFront() {
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
	
	public void insertAtFront(Integer elt) {
		if(isFull()) {
			throw new RuntimeException("Queue is full.");
		} else {
			if(isEmpty()) {
				rear = (rear+1) % capacity;
				front = (front+1) % capacity;
			} else {
				if(front==0) front = capacity-1;
				else front--;
			}
			q[front] = elt;
			size++;
		}
	}
	
	public Integer deleteFromRear() {
		if(isEmpty()) {
			throw new RuntimeException("Queue is empty.");
		} else {
			Integer frontItem = getFrontItem();		// Fetching item present at front, This is the item to be deleted.
			if(size==1) {
				rear=front=-1;
			} else {
				if(rear==0) rear = capacity-1;
				else rear--;
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
