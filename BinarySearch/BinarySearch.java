package binarySearch.basic;

public class BinarySearch {
	/*
	 A[] = {1, 2, 4, 5, 7, 8, 9};
	 */
	
	/**
	 * @param A - Input array. Array must be sorted in ascending order.
	 * @param key - Element to be searched.
	 * @return - Index of <b>{@code key}</b> if found, -1 otherwise.
	 */
	public static int binarySearch(Integer A[], Integer key){
		int mid, low=0, high=A.length-1;
		
		while(low<=high){
			mid = (high + low)/2;
			
			if(key==A[mid]){
				return mid;
			} else if(key<A[mid]) {	// Discard right half of underlying array.
				high = mid-1;
			} else if(key>A[mid]) {	// Discard left half of underlying array.
				low = mid+1;
			}
		}
		
		return -1;
	}
	
	/*
	 A[] = {8, 9, 1, 2, 4, 5, 7};
	 */
	
	/**
	 * @param A - Input array. Array must not contain duplicate elements and array must be circularly sorted. e.g-
	 * <p><code>A[] = {8, 9, 1, 2, 4, 5, 7}</code></p>
	 * @param key - Element to be searched.
	 * @return - Index of <b>{@code key}</b> if found, -1 otherwise.
	 */
	public static int binarySearchInCircularArray(Integer A[], Integer key) {
		int mid, low=0, high=A.length-1;
		
		while(low<=high){
			mid = (high + low)/2;
			
			if(key==A[mid])
				return mid;
			else if(A[low]<=A[mid]) {		// Left half is sorted.
				if(key>=A[low] && key<A[mid]){
					high = mid-1;
				} else{
					low = mid+1;
				}
			} else if(A[mid]<=A[high]) {	// Right half is sorted.
				if(key>A[mid] && key<=A[high]){
					low = mid+1;
				} else{
					high = mid-1;
				}
				
			}
		}
		return -1;
	}
	
	/*
	 A[] = {8, 9, 1, 2, 4, 5, 7};
	 */
	
	/**
	 * 
	 * @param A - Input array. Array must not contain duplicate elements and array must be circularly sorted. e.g-
	 * <p><code>A[] = {8, 9, 1, 2, 4, 5, 7}</code></p>
	 * @return - A numeric value indicating the number of times this <code>array</code> has been rotated,  
	 *  which is equal to the index of minimum element in this <code>array</code>.
	 *  <p>
	 *  	For example if <code>A[] = {8, 9, 1, 2, 4, 5, 7}</code><br/>
	 *  	then this function will return 2 (index of min. element). Which means that A is rotated 2 times.
	 *  </p>
	 */
	public static int rotateCountInCircularArray(Integer A[]) {
		int low = 0, high = A.length-1, mid;
		while(low<=high) {
			mid = (low+high)/2;
			
			if(A[mid] < A[mid-1]){
				if(A[mid] < A[mid+1]){	 // pivot property satisfied. And A[mid] is the minimum elt.
 					return mid;
				} else {							 // if A[mid] > A[mid+1]  then discard left half.
					low = mid + 1;
				}
			} else {								 // A[mid] > A[mid-1]
				if(A[mid] < A[mid+1]){	 // discard right half.
					high = mid -1;
				} else { 						 // if A[mid] > A[mid-1] then discard left half.
					low = mid + 1;
				}
			}
		}
		return -1;
	}
	
	public static void main(String[] args) {
		Integer A[] = {5, 7, 8, 9, 1, 2, 4}; //{8, 9, 1, 2, 4, 5, 7};
		System.out.println("Index : " + binarySearchInCircularArray(A, 9));
		System.out.println("This array has been rotated "+ rotateCountInCircularArray(A)+" times.");
	}
}
