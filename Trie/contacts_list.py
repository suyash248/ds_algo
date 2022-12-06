# https://www.youtube.com/watch?v=vlYZb68kAY0 - Contacts list

# Insert and search costs O(key_length), however the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N)
# where N is number of keys in Trie.

# https://www.youtube.com/watch?v=AXjmTQ8LEoI
class ContactNode(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        # Count of words (leaf nodes) starting from this node. It will help to find out the number of words/count starting with some prefix.
        self.wordsNum = 0

    def __str__(self):
        return "Children: {} | {}".format(self.children.keys(), self.endOfWord)


class Trie(object):
    def __init__(self):
        self.__root__ = ContactNode()

    # Time complexity: O(length_of_word)
    def insert(self, word):
        cur = self.__root__
        for ch in word:
            child = cur.children.get(ch, None)
            if child is None:
                child = ContactNode()
                cur.children[ch] = child
            child.wordsNum += 1
            cur = child
        cur.endOfWord = True

    # Time complexity: O(length_of_word)
    def search(self, word):
        cur = self.__root__
        for ch in word:
            child = cur.children.get(ch, None)
            if child is None:
                return False
            cur = child
        return cur.endOfWord

    def prefix_search_count(self, prefix):
        cur = self.__root__
        for ch in prefix:
            child = cur.children.get(ch, None)
            if child is None:
                return 0
            cur = child
        return cur.wordsNum

    # Time complexity: O(length_of_word)
    def __delete__(self, word, cur, index=0):
        if index == len(word):
            if cur.endOfWord:
                cur.endOfWord = False  # Mark `endOfWord` as we're going to delete this.
                return len(
                    cur.children) == 0  # If there are no children, delete this node (True means node will be deleted later)
            return False

        ch = word[index]
        child = cur.children.get(ch, None)
        # No need to check if this word exists or not as we've already checked it before calling this method.
        cur.wordsNum -= 1
        shouldRemove = self.__delete__(word, child, index=index + 1)

        # Removing node from memory (i.e. parent's `children' dict) if this is the only node remaining in `children1 dict.
        if shouldRemove:
            # Delete this node from memory, i.e. remove node corresponding to key(ch) from it's parent's `children` dict
            cur.children.pop(ch)

            # If parent's `children` dict becomes empty then parent is also a candidate for removal, return `True` in that case.
            return len(cur.children) == 0
        return False

    def delete(self, word):
        if self.search(word):
            self.__delete__(word, self.__root__)

    def __prefix_search__(self, prefix, joint_node):
        for ch, child_node in joint_node.children.items():
            prefix = prefix + ch
            if child_node.endOfWord:
                print
                prefix
            self.__prefix_search__(prefix, child_node)
            prefix = prefix[:-1]  # Backtracking

    def prefix_search(self, prefix):
        cur = self.__root__
        # Traverse till last character in `prefix`
        for ch in prefix:
            child = cur.children.get(ch, None)
            if child is None:
                return None
            cur = child
        self.__prefix_search__(prefix, cur)


if __name__ == '__main__':
    trie = Trie()
    choices = {
        1: "Add contact",
        2: "Search contact",
        3: "Prefix search(startswith) count",
        4: "Prefix search(startswith)",
        5: "Delete contact",
        6: "Exit"
    }
    choices = '\n'.join(['{}. {}'.format(k, v) for k, v in choices.items()])

    while True:
        print("\n" + choices + "\n")
        try:
            choice = int(input("Enter your choice - ")) or 0
        except:
            choice = 0

        if choice == 1:
            word = input("Please enter a contact name to be inserted - ")
            trie.insert(word)
        elif choice == 2:
            word = input("Please enter contact name to be searched - ")
            is_present = trie.search(word)
            print("{} is {}present".format(word, "" if is_present else "not "))
        elif choice == 3:
            prefix = input("Please enter a contact name/prefix to be searched - ")
            wordsNum = trie.prefix_search_count(prefix)
            print("There are {} contact(s) starting with prefix {}".format(wordsNum, prefix))
        elif choice == 4:
            prefix = input("Please enter a contact name/prefix to be searched - ")
            print("Contact(s) starting with prefix {} are -".format(prefix))
            trie.prefix_search(prefix)
        elif choice == 5:
            word = input("Please enter a word/sequence to be deleted - ")
            trie.delete(word)
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid choice")
            continue
