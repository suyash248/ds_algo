package sort.insertion;

import sort.AbstractBase;

/**
 * @author Suyash
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class InsertionSort extends AbstractBase {
	/*
	array[] = {5, 7, 1, 4, 2, 9, 3}
	5 7 1 4 2 9 3
	1 5 7 4 2 9 3
	1 4 5 7 2 9 3
	1 2 4 5 7 9 3
	1 2 4 5 7 9 3
	1 2 3 4 5 7 9
	*/
	public Integer[] sort(Integer array[]){
		int n=array.length, hole;
		int value;
		for(int i=1; i<n; i++){
			hole = i;
			value = array[i];
			while(hole>0 && array[hole-1]>value){
				array[hole] = array[hole-1];
				hole--;
			}
			array[hole] = value;
		}
		return array;
	}
	
	@Override
	public <E extends Comparable<E>> E[] genericSort(E[] array) {
		int n=array.length, hole;
		E value;
		for(int i=1; i<n; i++){
			hole = i;
			value = array[i];
			while(hole>0 && array[hole-1].compareTo(value)>0) {
				array[hole] = array[hole-1];
				hole--;
			}
			array[hole] = value;
		}
		return array;
	}
	
}
