package sort.quick;

import sort.AbstractBase;

/**
 * @author Suyash
 * <p>Complexity in average case is <b>O(nlog(n))</b>.</p>
 * <p>Complexity in worst case is <b>O(n^2)</b>.</p>
 */
public class QuickSort extends AbstractBase {

	public Integer[] sort(Integer array[], int start, int end){
		if(start<end){
			int pIndex = partition(array, start, end);
			sort(array, start, pIndex-1);
			sort(array, pIndex+1, end);
		}
		return array;
	}
	
	public int partition(Integer array[], int start, int end){
		/**
		All the elements <= pivot will be at the left of pIndex.
		*/
		int pIndex=start;
		int pivot = array[end], temp;
		for(int i=start; i<end; i++){
			if(array[i]<=pivot){
				// Swap array[pIndex] and current element.
				temp = array[pIndex];
				array[pIndex] = array[i];
				array[i] = temp;
				pIndex++;
			}
		}
		// Swap pivot(array[end]) and array[pIndex]
		temp = array[pIndex];
		array[pIndex] = array[end];
		array[end] = temp;
		return pIndex;
	}
	
	/******************************************************
											USING GENERICS
	 ******************************************************/
	
	public <E extends Comparable<E>> E[] genericSort(E[] array, int start, int end) {
		if(start<end) {
			int pIndex = partition(array, start, end);
			genericSort(array, start, pIndex-1);
			genericSort(array, pIndex+1, end);
		}
		return array;
	}
	
	public <E extends Comparable<E>> int partition(E[] array, int start, int end) {
		int pIndex = start;
		E pivot = array[end], temp;
		for(int i=start; i<end; i++){
			if(array[i].compareTo(pivot)<=0){
				// Swap array[pIndex] and current element.
				temp = array[i];
				array[i] = array[pIndex];
				array[pIndex] = temp;
				pIndex++;
			}
		}
		// Swap pivot(array[end]) and array[pIndex]
		temp = array[pIndex];
		array[pIndex] = array[end];
		array[end] = temp;
		return pIndex;
	}

}
