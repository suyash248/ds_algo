from fileCollection.file import File
from fileCollection.file_util import FileUtility

if __name__ == '__main__':
    file_utility: FileUtility = FileUtility()

    f1: File = File(name="f1", size=100)
    f2: File = File(name="f2", size=50)
    f3: File = File(name="f3", size=500)
    f4: File = File(name="f4", size=200)
    f5: File = File(name="f5", size=120)
    f6: File = File(name="f6", size=180)
    f7: File = File(name="f7", size=170)

    file_utility.save_files_to_collection("col1", f1, f2, f3)
    file_utility.save_files_to_collection("col2", f4, f5, f2)
    file_utility.save_files_to_collection("col3", f6, f1)
    file_utility.save_files_to_collection("col4", f3, f7)

    print(file_utility.get_total_size_processed())
    print(file_utility.get_top_k_collections(3))
