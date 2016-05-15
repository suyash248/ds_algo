package sort;

public abstract class AbstractBase {
	public <E extends Comparable<E>> E[] genericSort(E array[]) {return null;}
	public <E extends Comparable<E>> E[] genericSort(E[] array, int start, int end) {return null;}
	public <E> void printArray(E array[]){
		for(E elt : array){
			System.out.print(elt + " ");
		}
		System.out.println();
	}
}
