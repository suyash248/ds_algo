package custom.linked.list;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class DoublyLinkedList<T> {
	Node<T> start;
	
	public void addFirst(T elt){
		Node<T> newNode = new Node<T>(elt);
		newNode.prev = null;
		newNode.next = start;
		if(start!=null) // If this is not the first node to be inserted.
			start.prev = newNode;
		start = newNode;
	}
	
	public void addLast(T elt){
		Node<T> newNode = new Node<T>(elt);
		newNode.next = null;
		Node<T> i=start;
		for(; i.next!=null; i=i.next);
		i.next = newNode;
		newNode.prev = i;
	}

	public void add(T elt, int index){
		if(index==0)
			addFirst(elt);
		else{
			Node<T> node=start, backNode=start;
			for(int i=1; i<=index && node!=null; i++){
				backNode = node;
				node = node.next;
			}
			if(node!=null){
				Node<T> newNode = new Node<T>(elt);
				newNode.prev = backNode;
				newNode.next = node;
				
				backNode.next = newNode;
				node.prev = newNode;
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
		Node<T> i=start, backNode=start;
		for(; i!=null; i=i.next){
			if(i.value.equals(elt)){
				backNode.next = i.next;
				if(i.next!=null) i.next.prev = backNode;	// If it's not the last node.
				return true;
			}
			backNode = i;
		}
		return false;
	}
	
	@Override
	public String toString() {
		String asStr="start";
		for(Node<T> i=start; i!=null; i=i.next){
			asStr = asStr + " <--> " + i.getValue();
		}
		return asStr;
	}
	
	@Getter @Setter
	static class Node<T>{
		T value;
		Node<T> prev;
		Node<T> next;
		
		Node(){}
		Node(T value){
			this.value = value;
		}
	}
}
