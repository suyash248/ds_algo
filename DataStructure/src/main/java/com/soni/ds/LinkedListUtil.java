package com.soni.ds;

import com.soni.lib.SinglyLinkedList;
import com.soni.lib.SinglyLinkedList.Node;

public class LinkedListUtil {
	
	/**
	 * @param sll1 First linked list. @see {@link SinglyLinkedList}
	 * @param sll2 Second linked list. @see {@link SinglyLinkedList}
	 * @return String representation of merged linked list.
	 */
    public static String mergeSortedLinkedLists(SinglyLinkedList<Integer> sll1, SinglyLinkedList<Integer> sll2) {
    	Node<Integer> dummyNode = new Node<>();
    	Node<Integer> dummyNodeLast = dummyNode;
    	
    	Node<Integer> start1 = sll1.getStart();
    	Node<Integer> start2 = sll2.getStart();
    	
    	Node<Integer> i1 = start1, i2 = start2;
    	
    	while(true) {
    		Integer smallerVal = null;
    		if(i1!=null && i2!=null) {
	    		if(i1.getValue()<i2.getValue()) {
	    			smallerVal = i1.getValue();
	    			i1 = i1.getNext();
	    		} else {
	    			smallerVal = i2.getValue();
	    			i2 = i2.getNext();
	    		}
    		} else if(i1!=null) {
    			smallerVal = i1.getValue();
    			i1 = i1.getNext();
    		} else if(i2!=null) {
    			smallerVal = i2.getValue();
    			i2 = i2.getNext();
    		} else {
    			break;
    		}
    		
			Node<Integer> newNode = new Node<>(smallerVal, null);
			dummyNodeLast.setNext(newNode);
			dummyNodeLast = newNode;
    	}
    	
    	String allElts="start";
		Node<Integer> i;
		for(i = dummyNode.getNext(); i!=null; i=i.getNext()){
			allElts = allElts + "->"+i.getValue();
		}
		return allElts;
    }
}
