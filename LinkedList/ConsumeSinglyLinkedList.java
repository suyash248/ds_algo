package custom.linked.list;

public class ConsumeSinglyLinkedList {
	public static void main(String[] args) {
		SinglyLinkedList<Integer> sll = new SinglyLinkedList<Integer>();
		sll.addFirst(1);
		sll.addLast(2);
		sll.addLast(3);
		sll.addLast(4);
		sll.addLast(5);
		sll.addLast(6);
		sll.addLast(7);
		sll.addLast(8);
		sll.addFirst(0);
		
		sll.add(50, 2);
		
		sll.delete(50);
		System.out.println(sll);
	}
}
