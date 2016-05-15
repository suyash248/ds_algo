package sort.bubble;

import sort.AbstractBase;

/**
 * @author Suyash
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class BubbleSort extends AbstractBase{
	/*
	array[] = {5, 7, 1, 4, 2, 9, 3}
	1 4 2 5 3 7 9 
	1 2 4 3 5 7 9 
	1 2 3 4 5 7 9 
	1 2 3 4 5 7 9 
	1 2 3 4 5 7 9 
	1 2 3 4 5 7 9 
	*/
	public Integer[] basicBubbleSort(Integer array[]){
		int n = array.length;
		int temp;
		for(int i=0; i<n ; i++){
			for(int j=0; j<(n-i-1); j++){
				if(array[j]>array[j+1]){
					temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
				}
			}
			//this.printArray(array);
		}
		return array;
	}
	
	/*
	array[] = {5, 7, 1, 4, 2, 9, 3}
	5 1 4 2 7 3 9 
	1 4 2 5 3 7 9 
	1 2 4 3 5 7 9 
	1 2 3 4 5 7 9 
	 */
	public Integer[] optimizedBubbleSort(Integer array[]){
		int n = array.length;
		int temp;
		boolean sorted;	// This flag will stop/break the loop once elements are sorted.
		for(int i=0; i<n ; i++){
			sorted = true;
			for(int j=0; j<(n-i-1); j++){
				if(array[j]>array[j+1]){
					temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
					sorted = false;
				}
			}
			if(sorted) break;
			// this.printArray(array);
		}
		return array;
	}

	@Override
	public <E extends Comparable<E>> E[] genericSort(E[] array) {
		int n=array.length;
		E temp;
		boolean sorted;
		for(int i=0; i<n; i++){
			sorted = true;
			for(int j=0; j<(n-i-1); j++){
				if(array[j].compareTo(array[j+1])>0){
					temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
					sorted = false;
				}
			}
			if(sorted) break;
			// this.printArray(array);
		}
		return array;
	}
}
