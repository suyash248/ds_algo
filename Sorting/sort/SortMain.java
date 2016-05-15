package sort;

import sort.quick.QuickSort;

public class SortMain {
	public static void main(String[] args) {
		
		AbstractBase base = new QuickSort();
		QuickSort qs = (QuickSort) base;
		
		Integer arrayInteger[] = {5, 7, 1, 4, 2, 9, 3};
		arrayInteger = qs.sort(arrayInteger, 0, arrayInteger.length-1);
		base.printArray(arrayInteger);
				
		String arrayString[] = {"Suyash", "Anoop", "Virag", "Sunny", "Abhishek", "Saurabh", "Ramya"};
		arrayString = base.genericSort(arrayString, 0, arrayString.length-1);
		base.printArray(arrayString);
	}
}
