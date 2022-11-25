from uuid import uuid4


class File(object):
    def __init__(self, size: int, name: str = None):
        self.size = size
        self.name = name or str(uuid4())

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "({} - {})".format(self.name, self.size)

    def __repr__(self):
        return self.__str__()
