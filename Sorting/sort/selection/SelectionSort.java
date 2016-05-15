package sort.selection;

import sort.AbstractBase;

/**
 * @author Suyash
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class SelectionSort extends AbstractBase {	
	/*
	 array[] = {5, 7, 1, 4, 2, 9, 3}
	 1 7 5 4 2 9 3 
	 1 2 5 4 7 9 3 
	 1 2 3 4 7 9 5 
	 1 2 3 4 7 9 5 
	 1 2 3 4 5 9 7 
	 1 2 3 4 5 7 9 
	 1 2 3 4 5 7 9 
	*/
	
	public Integer[] sort(Integer array[]){
		int n = array.length, temp, imin;
		for(int i=0; i<(n-1); i++){
			imin = i;
			for(int j=i+1; j<n; j++){
				if(array[j]<array[imin]){
					imin = j;
				}
			}
			temp = array[i];
			array[i] = array[imin];
			array[imin] = temp;
			// sel.printArray(array);
		}
		return array;
	}
	
	@Override
	public <E extends Comparable<E>> E[] genericSort(E array[]){
		int n = array.length, imin;
		E temp;
		for(int i=0; i<(n-1); i++){
			imin=i;
			for(int j=i+1; j<n; j++){
				if(array[j].compareTo(array[imin])<0) {
					imin = j;
				}
			}
			temp = array[i];
			array[i] = array[imin];
			array[imin] = temp;
			// sel.printArray(array);
		}
		return array;
	}	
	
}