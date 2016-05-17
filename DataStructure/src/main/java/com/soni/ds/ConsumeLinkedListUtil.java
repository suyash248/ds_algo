package com.soni.ds;

import com.soni.lib.SinglyLinkedList;

public class ConsumeLinkedListUtil {
	public static SinglyLinkedList<Integer> sll1 = new SinglyLinkedList<Integer>();
	public static SinglyLinkedList<Integer> sll2 = new SinglyLinkedList<Integer>();
	static {
		sll1.addFirst(1);
		sll1.addLast(4);
		sll1.addLast(5);
		sll1.addLast(7);
		sll1.addLast(9);
				
		System.out.println("List-1 : " + sll1);
		
		sll2.addLast(2);
		sll2.addLast(3);
		sll2.addLast(6);
		sll2.addLast(8);
				
		System.out.println("List-2 : " + sll2);
	}
	
    public static void main( String[] args ) {
    	System.out.println("Before deletion : " + sll1);
    	LinkedListUtil.deleteNode(sll1.getStart().getNext());
    	System.out.println("After deletion : " + sll1);
    }
}
