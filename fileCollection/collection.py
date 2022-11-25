from typing import Set, List
from fileCollection.file import File


class Collection(object):
    def __init__(self, name: str, files: Set[File] = None):
        self.name = name
        self.files = files or set()
        self.totalSize = 0
        self.sub_collections: List[Collection] = []

    def add_file(self, file: File) -> bool:
        if file not in self.files:
            self.files.add(file)
            self.totalSize += file.size
            return True
        return False

    def __str__(self):
        return "({}, Size: {}, Files: {})".format(self.name, self.totalSize, len(self.files))

    def __repr__(self):
        return self.__str__()

