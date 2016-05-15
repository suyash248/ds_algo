package custom.linked.list;

public class ConsumeDoublyLinkedList {
	public static void main(String[] args) {
		DoublyLinkedList<Integer> dll = new DoublyLinkedList<Integer>();
		dll.addFirst(1);
		dll.addLast(2);
		dll.addLast(3);
		dll.addLast(4);
		dll.addLast(5);
		dll.addLast(6);
		dll.addLast(7);
		dll.addLast(8);
		dll.addFirst(0);
		
		dll.add(50, 2);
		
		dll.delete(50);
		System.out.println(dll);
	}
}
