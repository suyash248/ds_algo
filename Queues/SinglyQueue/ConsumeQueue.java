package queue.array;

public class ConsumeQueue {
	public static void main(String[] args) {
		QueueUsingArray q = new QueueUsingArray(7);
		q.insert(2);
		q.insert(8);
		q.insert(1);
		q.insert(4);
		q.insert(9);
		q.insert(7);
		q.insert(5);
		System.out.println(q);
		
		q.delete();
		q.delete();
		q.delete();
		q.insert(3);
		System.out.println(q);
		
		System.out.println("Capacity : "+q.getCapacity() + " | Size : "+ q.getSize());
		System.out.println("Front item : "+q.getFrontItem() + " | Rear item : "+q.getRearItem());
		
	}
}
