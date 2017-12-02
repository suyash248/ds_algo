package custom.hashtable;

public class ConsumeHashtable {
	public static void main(String... w) {
		CustomHashtable<Integer, String> hashTable = new CustomHashtable<Integer, String>(20);
		hashTable.put(10, "Ramu");
		hashTable.put(6, "Lanka");
		hashTable.put(3, "Vishu");
		hashTable.put(7, "Sood");
		hashTable.put(1, "Sashi");
		hashTable.put(5, "Nareddi");
		hashTable.put(2, "Dhar");
		hashTable.put(3, "Sona");
		hashTable.put(20, "Chaandi");
		hashTable.put(12, "Silver");
		hashTable.put(9, "Gold");
		hashTable.put(89, "Smith");
		hashTable.put(15, "Iron");
		hashTable.put(90, "Bronze");
		hashTable.put(14, "Metal");
		hashTable.put(80, "Hyderabad");
		hashTable.put(60, "Ramya");
		hashTable.put(70, "Telangana");
		
		hashTable.remove(10);
		System.out.println("Size : "+hashTable.getSize()+"\n"+hashTable);		
		
		//System.out.println(hashTable.get(90));
	}
}
