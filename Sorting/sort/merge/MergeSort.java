package sort.merge;

import java.lang.reflect.Array;
import java.util.Arrays;

import sort.AbstractBase;

/**
 * @author Suyash
 * <p>Complexity in worst case is <b>O(nlog(n))</b>.</p>
 */
public class MergeSort extends AbstractBase  {
	/*
	array[] = {5, 7, 1, 4, 2, 9, 3}
	*/
	public Integer[] sort(Integer array[]){
		int n=array.length, i, j;
		int mid = n/2;
		Integer left[] = new Integer[mid];
		Integer right[] = new Integer[n-mid];
		
		for(i=0; i<mid; i++){
			left[i] = array[i];
		}
		for(j=mid; j<n; j++){
			right[j-mid] = array[j];
		}
		
		if(n<2){
			return array;
		} else{
			sort(left);
			sort(right);
			array = merge(left, right, array);
			left=right=null;
			return array;
		}
	}

	private Integer[] merge(Integer left[], Integer right[], Integer array[]){
		int iL=0, iR=0, iA=0;
		int nL = left.length, nR = right.length;
		while(iL<nL && iR<nR){
			if(left[iL]<=right[iR]){
				array[iA] = left[iL];
				iL++;
			} else {
				array[iA] = right[iR];
				iR++;
			}
			iA++;
		}
		
		while(iL<nL){
			array[iA] = left[iL];
			iL++;
			iA++;
		}
		while(iR<nR){
			array[iA] = right[iR];
			iR++;
			iA++;
		}
		return array;
	}
	
	
	/******************************************************
											USING GENERICS
	 ******************************************************/
	/*
	    array = [ Suyash Anoop Virag Sunny Abhishek Saurabh ]
		[ Suyash Anoop Virag ]       &     [ Sunny Abhishek Saurabh ]   =   [ Suyash Anoop Virag Sunny Abhishek Saurabh ]      
		[ Suyash ]       &     [ Anoop Virag ]   =   [ Suyash Anoop Virag ]      
		[ Anoop ]       &     [ Virag ]   =   [ Anoop Virag ]      
		[ Sunny ]       &     [ Abhishek Saurabh ]   =   [ Sunny Abhishek Saurabh ]      
		[ Abhishek ]       &     [ Saurabh ]   =   [ Abhishek Saurabh ]      
	 */
	@Override
	public <E extends Comparable<E>> E[] genericSort(E[] array) {
		int n=array.length;
		int mid = n/2;
		E[] left = Arrays.copyOfRange(array, 0, mid);
		E[] right = Arrays.copyOfRange(array, mid, n);
		if(n<2){
			return array;
		} else{
			genericSort(left);
			genericSort(right);
			array = merge(left, right, array);
			left=right=null;
			return array;
		}
	}
	
	/*
 	[ Anoop ]   &   [ Virag ]   =   [ Anoop Virag ]      
	[ Suyash ]   &   [ Anoop Virag ]   =   [ Anoop Suyash Virag ]      
	[ Abhishek ]   &   [ Saurabh ]   =   [ Abhishek Saurabh ]      
	[ Sunny ]   &   [ Abhishek Saurabh ]   =   [ Abhishek Saurabh Sunny ]      
	[ Anoop Suyash Virag ]   &   [ Abhishek Saurabh Sunny ]   =   [ Abhishek Anoop Saurabh Sunny Suyash Virag ]      
	Abhishek Anoop Saurabh Sunny Suyash Virag 
 */
	public <E extends Comparable<E>> E[] merge(E left[], E right[], E array[]) {
		int nL = left.length, nR = right.length;
		int iL = 0,iR = 0, iA=0;
		while(iL<nL && iR<nR){
			if( (left[iL].compareTo(right[iR])) <=0){
				array[iA] = left[iL];
				iL++;
			} else{
				array[iA] = right[iR];
				iR++;
			}
			iA++;
		}
		
		while(iL<nL){
			array[iA] = left[iL];
			iL++;
			iA++;
		}
		
		while(iR<nR){
			array[iA] = right[iR];
			iR++;
			iA++;
		}
	
		return array;
	}

}



//Printing logic just for testing.
/*System.out.print("[ ");
for(E eL : left){
	System.out.print(eL+" ");
}
System.out.print("]      ");

System.out.print(" &     [ ");
for(E eR : right){
	System.out.print(eR+" ");
}
System.out.print("]   =   ");

System.out.print("[ ");
for(E eA : array){
	System.out.print(eA+" ");
}
System.out.print("]      \n");
*/