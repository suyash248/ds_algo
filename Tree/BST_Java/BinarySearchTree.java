package tree.bst;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

import lombok.Getter;

/**
 * Binary search tree (BST) implementation along with utility functions for performing various operations on BST.
 * @author Suyash
 */
public class BinarySearchTree {
	
	/**
	 * <code>root</code> node of this BST.
	 */
	@Getter
	public Node root;
	
	private  Node prev=null;
	private List<Integer> inorderList = new ArrayList<Integer>();
	
	/**
	 *  Inserts a node in BST using iterative approach.
	 * @param data - data to be inserted.
	 */
	public void insertIterative(Integer data){
		Node newNode = new Node(data);
		// If root is null, it indicates tree is empty.
		if(root==null){
			root = newNode;
			return;
		} 
		
		Node temp = root;
		
		while(true) {
			// If data to be inserted is less than current node's data, Insert this new node in left subtree.
			if(data < temp.data) {
				if(temp.left != null) {
					temp = temp.left;
				} else {
					temp.left = newNode;
					break;
				}
			}
			// If data to be inserted is greater than current node's data, Insert this new node in right subtree.
			else if(data > temp.data) {
				if(temp.right != null) {
					temp = temp.right;
				} else {
					temp.right = newNode;
					break;
				}
			}
		}
	}
	
	/**
	 * Inserts a node in BST using recursive approach. 
	 * @param data - data to be inserted.
	 * @param current - <code>root</code> node.
	 */
	public Node insertRecursive(Integer data, Node current){
		if(current==null) {
			Node newNode = new Node(data);
			current = newNode;
		} else if(data <= current.data) {	// If data to be inserted is less than current node's data, Insert this new node in left subtree.
			current.left = insertRecursive(data, current.left);
		} else if(data > current.data) {		// If data to be inserted is greater than current node's data, Insert this new node in right subtree.
			current.right = insertRecursive(data, current.right);
		}
		return current;
	}
	
	/**
	 * <i>Recursively</i> checks if data a node containing <code>data</code> is present in this BST.
	 * @param data - Data to be searched.
	 * @return - <code>true</code> if data is found, <code>false</code> otherwise.
	 */
	public boolean searchIterative(int data) {
		Node temp = root;
		while(temp!=null) {
			if (data == temp.data){			// Data found.
				return true;
			} else if (data < temp.data) {	// If data being searched is less than current node's data then search in left subtree.
				temp = temp.left;
			} else if (data > temp.data) {	// If data being searched is greater than current node's data then search in right subtree.
				temp = temp.right;
			} else {
				return false;
			}
		}
		return false;
	}
	
	/**
	 * <i>Iteratively</i> checks if data a node containing <code>data</code> is present in this BST.
	 * @param data - Data to be searched.
	 * @return - <code>true</code> if data is found, <code>false</code> otherwise.
	 */
	public boolean searchRecursive(Node current, int data) {
		if(current==null) {												// Data not found.
			return false;
		}
		if(data==current.data) {										// Data found.
			return true;
		} else if(data < current.data) {								// If data being searched is less than current node's data then search in left subtree.
			return searchRecursive(current.left, data);
		} else { //  if(data > current.data)
			return searchRecursive(current.right, data);	// If data being searched is greater than current node's data then search in right subtree.
		}
	}
	
	/**
	 * <b>Category : </b>BFS (Breadth-First-Search).<br/>
	 *  <p>All the node at a level are traversed before moving to next level. In other words, Nodes
	 *  will be traversed level-by-level. </p>
	 */
	public void levelOrderTraversal() {
		Queue<Node> q = new ArrayDeque<Node>();
		q.add(root);
		while(q.size()>0) {
			Node node = q.poll();
			System.out.print(node.data+" ");
			if(node.left != null) {
				q.add(node.left);
			}
			if(node.right != null) {
				q.add(node.right);
			}
		}
	}
	
	/**
	 * <b>Category : </b>DFS (Depth-First-Search).<br/>
	 * <p>Traversal order : <b>Root --> Left subtree --> Right-subtree</b> </p>
	 * @param current - <code>root</code> node.<br/>
	 */
	public void preOrderTraversal(Node current) {
		if(current==null)
			return;
		
		System.out.print(current.data+" ");
		preOrderTraversal(current.left);
		preOrderTraversal(current.right);
	}
	
	/**
	 * <b>Category : </b>DFS (Depth-First-Search).<br/>
	 * <p>Traversal order : <b>Left subtree --> Root --> Right-subtree</b> </p>
	 * <b>Note : </b> All the nodes will be traversed in a sorted order.
	 * @param current - <code>root</code> node.<br/>
	 */
	public void inOrderTraversal(Node current) {
		if(current==null)
			return;
		
		inOrderTraversal(current.left);
		System.out.print(current.data+" ");
		inOrderTraversal(current.right);
	}
	
	/**
	 * <b>Category : </b>DFS (Depth-First-Search).<br/>
	 * <p>Traversal order : <b>Left subtree  --> Right-subtree --> Root</b> </p>
	 * @param current - <code>root</code> node.<br/>
	 */
	public void postOrderTraversal(Node current) {
		if(current==null)
			return;
		
		postOrderTraversal(current.left);
		postOrderTraversal(current.right);
		System.out.print(current.data+" ");
	}
	
	/** 
	 * This method finds out the minimum element using <i>iterative</i> approach.
	 * @return Minimum element.
	 */
	public Integer findMinIterative() {
		Node temp = root;
		if(temp==null) {
			throw new RuntimeException("Tree is empty.");
		} else {
			while(temp.left!=null) {
				temp=temp.left;
			}
			return temp.data;
		}
	}
	
	/** 
	 * This method finds out the minimum element using <i>recursive</i> approach.
	 * @param current - <code>root</code> node.<br/>
	 * @return Minimum element.
	 */
	public Integer findMinRecursive(Node current) {
		if(current==null){
			throw new RuntimeException("Tree is empty.");
		} else {
			if(current.left==null) {
				return current.data;
			} else {
				return findMinRecursive(current.left);
			}
		}
	}
	
	/** 
	 * This method finds out the maximum element using <i>iterative</i> approach.
	 * @return Maximum element.
	 */
	public Integer findMaxIterative() {
		Node temp = root;
		if(temp==null) {
			throw new RuntimeException("Tree is empty.");
		} else {
			while(temp.right!=null) {
				temp=temp.right;
			}
			return temp.data;
		}
	}
	
	/** 
	 * This method finds out the maximum element using <i>recursive</i> approach.
	 * @param current - <code>root</code> node.<br/>
	 * @return Maximum element.
	 */
	public Integer findMaxRecursive(Node current) {
		if(current==null){
			throw new RuntimeException("Tree is empty.");
		} else {
			if(current.right==null) {
				return current.data;
			} else {
				return findMaxRecursive(current.right);
			}
		}
	}
	/**
	 * Calculates the height/maximum depth of tree <i>recursively</i>.
	 * @param current <code>root</code> node.
	 * @return Height of tree. i.e. height of <code>root</code> node. This is also equal to the maximum <i>depth</i> of the tree.
	 */
	public Integer findHeightRecursive(Node current) {
		if(current==null) {
			return -1;		// Height of root nodes is 0;
		}
		// Calculate height of left subtree.
		int leftHeight = findHeightRecursive(current.left);
		
		// Calculate height of right subtree.
		int rightHeight = findHeightRecursive(current.right);	
		
		// Height of node = Maximum of leftHeight(Height of it's left subtree) & rightHeight(Height of it's right subtree).
		int max = Math.max(leftHeight, rightHeight);
		return max + 1;
	}
	
	/**
	 * Calculates the height/maximum depth of tree <i>iteratively</i>.
	 * @return Height of tree. i.e. height of <code>root</code> node. This is also equal to the maximum <i>depth</i> of the tree.
	 */
	public Integer findHeightIterative() {
		Queue<Node> q = new ArrayDeque<Node>();
		
		// Enqueue Root and initialize height.
		q.add(root);
		int height=0, size;
		
		// size (queue size) indicates number of nodes at current level.
		
		while(true) {
			size = q.size();
			if(size==0)
				return height-1;
			else {
				height++;
				
				// Dequeue all nodes of current level and Enqueue all nodes of next level
				while(size>0) {
					Node node = q.poll();	// Retrieve and removes an element from the head/front of this queue.
					if(node.left != null) {
						q.add(node.left);		// Enqueue the left node at next level, it is not null.
					} 
					if(node.right != null) {
						q.add(node.right); 	// Enqueue the right node at next level, it is not null.
					}
					size--;
				}
			}
		}
	}
	
	/**
	 * @return <code>true</code> if this is BST, <code>false</code> otherwise.
	 */
	public boolean isBST() {
		return isBstUtill(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
	}
	/**
	 * 
	 * @param current - <code>root</code> node.
	 * @param minVal - <code>java.lang.Integer.MIN_VALUE</code>
	 * @param maxVal - <code>java.lang.Integer.MAX_VALUE</code>
	 * @return <code>true</code> if data inside all nodes lies in permissible range. <code>false</code> otherwise.
	 */
	private boolean isBstUtill(Node current, int minVal, int maxVal) {
		if(current==null) {
			return true;
		}
		if(current.data <= maxVal && 
				current.data > minVal && 
				isBstUtill(current.left, minVal, current.data) && 
				isBstUtill(current.right, current.data, maxVal) ) {
			return true;
		} else{
			return false;
		}
	}
	
	/**
	 * @return <code>true</code> if this is BST, <code>false</code> otherwise.
	 */
	public boolean isBSTUsingInorderWithExtraArray() {
		inorderTraversalList(root);
		for(int i=0; i<inorderList.size()-1; i++){
			if(inorderList.get(i) > inorderList.get(i+1)){
				return false;
			}
		}
		return true;
	}
	
	/**
	 * Performs in-order traversal and add each node in a <code>java.util.List</code>.
	 * @param current - <code>root</code> node.
	 */
	private void inorderTraversalList(Node current) {
		if(current==null)
			return;
		
		inorderTraversalList(current.left);
		inorderList.add(current.data);
		inorderTraversalList(current.right);
	}
	
	/**
	 * @return <code>true</code> if this is BST, <code>false</code> otherwise.
	 */
	public boolean isBSTUsingInorder() {
		return isBSTUtil(root);
	}
	
	/** 
	 * <p>If using in-order traversal nodes are visited in sorted order then underlying tree is a BST.</p>
	 * Performs in-order traversal and keep track of previous node traversed. 
	 * <ul>
	 * 	<li>if previous node is <code>lesser</code> than the current node then we are visiting the nodes in sorted order. Continue with traversal.</li>
	 * 	<li>But if previous node is <code>greater</code> than the current node then we are visiting the nodes in sorted order. exit and return <code>false</code> </li>
	 * </ul>
	 * @param current - <code>root</code> node.
	 * @return <code>true</code> if this is BST, <code>false</code> otherwise.
	*/
	private boolean isBSTUtil(Node current) {
		if(current==null)
			return true;
		
		if(!isBSTUtil(current.left))
			return false;
		if(prev != null && current.data <= prev.data) {
			return false;
		}
		prev = current;
		return isBSTUtil(current.right);
	}
	
	/**
	 * Deletes a node from BST.
	 * @param current - <code>root</code> node.
	 * @param data - Data to be deleted.
	 * @return -  <code>root</code> node, as  <code>root</code> might change after deletion.
	 */
	public Node delete(Node current, int data) {
		if(current==null) return current;
		
		// If data in a node to be deleted is lesser than data in current node then target node is in left sub-tree.
		else if(data < current.data) {
			current.left = delete(current.left, data);
		}
		
		// If data in a node to be deleted is greater than data in current node then target node is in right sub-tree.
		else if(data > current.data) {
			current.right = delete(current.right, data);
		} 
		
		// If data in a node to be deleted is equal to data in current node then, we found the target node, 
		// Now go ahead and delete it.
		else {	// data == current.data
		
			// node with only one child or no child 
			if(current.left == null) {
				current = current.right;
			}
			else if(current.right == null) {
				current = current.left;
			}
			
			// node with 2 children
			else {
				// There are following 2 approaches-
				
				// Approach - 1 : Through in-order successor.
				// Find In-order successor, i.e. min. element from right subtree and copy it's data to current node's data.
				// Then delete that in-order successor. 
				// Since In-order successor is a min. element in a sub-tree so In-order successor will never have left child though it may or may not have right child.
				// Clearly in-order successor will have either 0 or 1 child, Hence deleting in-order successor is either Case-1 or Case-2.
				
				// Approach - 2 : Through in-order predecessor.
				// We could also find In-order predecessor, i.e. max. element from left subtree and copy it' data to current node's data.
				// Then delete that in-order predecessor.
				// Since In-order predecessor is a max. element in a sub-tree so In-order predecessor will never have right child though it may or may not have left child.
				// Clearly in-order predecessor will have either 0 or 1 child, Hence deleting in-order predecessor is either Case-1 or Case-2.
				
				// Here we'll go with Approach-1.
				
				int inOrderSuccessorData = findMinRecursive(current.right);	// Finding in-order successor.
				current.data = inOrderSuccessorData;										// Copying the data of in-order successor to current node.
				current.right = delete(current.right, inOrderSuccessorData);		// deleting the in-order successor.
			}
		}
		return current;
	}
	
	public Node findInOrderSuccessor(Node rootNode, int data) {
		if(rootNode==null) return null;
		Node targetNode = find(data);
		
		if(targetNode.right!=null) {								// Case-1 : Current node has right subtree.
			return findMin(targetNode.right);
		} else {															// Case-2 : Current node doesn't have right subtree.
			Node ancestor = root;
			Node successor = null;
			while(ancestor != targetNode) {
				if(targetNode.data < ancestor.data) {
					successor = ancestor;
					ancestor = ancestor.left;
				} else {
					ancestor = ancestor.right;
				}
			}
			return successor;
		}
	}
	private Node find(int data) {
		Node temp = root;
		while(temp!=null) {
			if(data < temp.data) {
				temp = temp.left;
			} else if(data > temp.data) {
				temp = temp.right;
			} else {
				return temp;
			}
		}
		return null;
	}
	private Node findMin(Node current) {
		if(current==null) return null;
		
		while(current.left!=null) {
			current = current.left;
		}
		return current;
	}
	
	@Getter
	static class Node{
		private Integer data;
		private Node left;
		private Node right;
		public Node(Integer data) {
			this.data = data;
			left = right = null;
		}
	}
}
