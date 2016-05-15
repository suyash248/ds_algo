package deque.array;

public class ConsumeQueue {
	public static void main(String[] args) {
		DequeUsingArray dq = new DequeUsingArray(7);
		dq.insertAtFront(2);
		dq.insertAtFront(1);
		dq.insertAtRear(3);
		dq.insertAtRear(4);
		dq.insertAtRear(5);
		dq.insertAtRear(6);
		dq.insertAtFront(0);
		
		System.out.println(dq);
		
		dq.deleteFromRear();
		dq.insertAtFront(7);
		dq.deleteFromFront();
		dq.insertAtFront(8);
		
		System.out.println(dq);
		System.out.println("Capacity : "+dq.getCapacity() + " | Size : "+ dq.getSize());
		System.out.println("Front item : "+dq.getFrontItem() + " | Rear item : "+dq.getRearItem());
	}
}
