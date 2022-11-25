from typing import Dict
from fileCollection.collection import Collection
from fileCollection.file import File


class FileUtility(object):
    def __init__(self):
        self.total_size_processed: int = 0
        self.collections: Dict[str, Collection] = dict()

    def save_file_to_collection(self, collection_name: str, file: File):
        collection: Collection = self.get_or_create_collection(collection_name)
        is_added = collection.add_file(file)
        if is_added:
            self.total_size_processed += file.size

    def save_files_to_collection(self, collection_name: str, *files):
        for file in files:
            self.save_file_to_collection(collection_name, file)

    def get_or_create_collection(self, collection_name: str) -> Collection:
        collection_name = collection_name.lower()
        if collection_name not in self.collections:
            self.collections[collection_name] = Collection(collection_name)
        return self.collections[collection_name]

    def get_total_size_processed(self) -> int:
        return self.total_size_processed

    def get_top_k_collections(self, k: int):
        return list(sorted(self.collections.values(), key=lambda col: col.totalSize, reverse=True))[:k]

