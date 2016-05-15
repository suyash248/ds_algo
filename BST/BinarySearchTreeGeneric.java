package tree.bst;

import lombok.Getter;

public class BinarySearchTreeGeneric<E extends Comparable<E>> {
	@Getter
	Node<E> root;
	
	public void insert(E data){
		Node<E> newNode = new Node<E>(data);

	}
	
	static class Node<E extends Comparable<E>>{
		E data;
		Node<E> left;
		Node<E> right;
		Node(E data) {
			this.data = data;
			left = right = null;
		}
	}
}
