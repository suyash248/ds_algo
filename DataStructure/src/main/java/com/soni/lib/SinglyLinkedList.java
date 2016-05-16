package com.soni.lib;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class  SinglyLinkedList<T> {
	private Node<T> start;
	
	public void addFirst(T elt){
		Node<T> newNode = new Node<T>();
		newNode.setValue(elt);
		newNode.setNext(start);
		start = newNode;
	}
	
	public void addLast(T elt){
		if(start != null){
			Node<T> i;
			for(i = start; i.next!=null; i = i.next);
			Node<T> newNode = new Node<T>(elt, i.next);
			i.next = newNode;
		} else
			addFirst(elt);
	}
	
	public void add(T elt, int index){
		if(index==0)
			addFirst(elt);
		else{
			Node<T> node = start, backNode=start;
			for(int i=0; i<index && node.next!=null; i++){
				backNode = node;
				node = node.next;
			}
			if(node.next!=null){
				Node<T> newNode = new Node<T>(elt, node);
				backNode.next = newNode;
			} else{
				addLast(elt);
			}
		}
	}
	
	public boolean delete(T elt){
		if(start.getValue().equals(elt)){
			start = start.next;
			return true;
		}
		Node<T> backNode=start;
		for(Node<T> i=start; i!=null; i=i.next){
			if(i.value.equals(elt)){
				backNode.next = i.next;
				return true;
			}
			backNode = i;
		}
		return false;
	}
	
	@Override
	public String toString() {
		String allElts="start";
		Node<T> i;
		for(i = start; i!=null; i=i.next){
			allElts = allElts + "->"+i.getValue();
		}
		return allElts;
	}
	
	@Getter @Setter
	public static class Node<T> {
		T value;
		Node<T> next;
		public Node(T value, Node<T> next){
			this.value = value;
			this.next = next;
		}
		public Node(){}
	}
}
