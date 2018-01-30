package tree.bst;

public class ConsumeTree {
	public static void main(String[] args) {
		BinarySearchTree bst = new BinarySearchTree();
		bst.root = bst.insertRecursive(25, bst.root);
		bst.root = bst.insertRecursive(15, bst.root);
		bst.root = bst.insertRecursive(17, bst.root);
		bst.root = bst.insertRecursive(18, bst.root);
		bst.root = bst.insertRecursive(10, bst.root);
		bst.root = bst.insertRecursive(30, bst.root);
		bst.root = bst.insertRecursive(26, bst.root);
		bst.root = bst.insertRecursive(31, bst.root);
		bst.root = bst.insertRecursive(27, bst.root);
		
		System.out.println("Element found : "+bst.searchRecursive(bst.root, 15));
		System.out.println("Minimum : "+bst.findMinRecursive(bst.root) + " | Maximum : "+bst.findMaxRecursive(bst.root));
		System.out.println("Height or Maximum depth : "+bst.findHeightIterative());
		System.out.print("Level Order Traversal : "); bst.levelOrderTraversal();
		System.out.print("\nPre-Order Traversal : "); bst.preOrderTraversal(bst.root);
		System.out.print("\nIn-Order Traversal : "); bst.inOrderTraversal(bst.root);
		System.out.print("\nPost-Order Traversal : "); bst.postOrderTraversal(bst.root);
		
		System.out.println("\nIs BST : "+bst.isBST());
		System.out.println("Is BST (Using inorder) : "+bst.isBSTUsingInorder());
		System.out.println("Is BST (Using inorder with extra array/list) : "+bst.isBSTUsingInorderWithExtraArray());
		
		System.out.println("Root after deletion : " + bst.delete(bst.root, 18).getData());
		System.out.print("In-Order traversal after deletion : "); bst.inOrderTraversal(bst.root);
		
		Integer successor = bst.findInOrderSuccessor(bst.root, 15) != null ? bst.findInOrderSuccessor(bst.root, 15).getData() : null;
		System.out.println("\nIn-Order successor : "+successor);

	}
}


/*Node n = new Node(10);
bst.root = n;
n.left = new Node(20);
n.right = new Node(30);*/
