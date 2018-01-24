# Insert and search costs O(key_length), however the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N)
# where N is number of keys in Trie.

# https://www.youtube.com/watch?v=AXjmTQ8LEoI
class _Node(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def __str__(self):
        return "Children: {} | {}".format(self.children.keys(), self.endOfWord)

class Trie(object):
    def __init__(self):
        self.__root__ = _Node()


############################### INSERT ###############################


    # Time complexity: O(length_of_word)
    def insert(self, word):
        cur = self.__root__
        for ch in word:
            #print ch,
            child = cur.children.get(ch, None)
            if child is None:
                child = _Node()
                cur.children[ch] = child
            cur = child
        cur.endOfWord = True

    # Time complexity: O(length_of_word)
    def __insert_recursive__(self, word, cur, index=0):
        if index == len(word):
            cur.endOfWord = True
            return
        ch = word[index]
        child = cur.children.get(ch, None)
        if child is None:
            child = _Node()
            cur.children[ch] = child
        self.__insert_recursive__(word, child, index=index+1)

    def insert_recursive(self, word):
        self.__insert_recursive__(word, self.__root__)


############################### SEARCH (Whole word) ###############################


    # Time complexity: O(length_of_word)
    def search(self, word):
        cur = self.__root__
        for ch in word:
            child = cur.children.get(ch, None)
            if child is None:
                return False
            cur = child
        return cur.endOfWord

    # Time complexity: O(length_of_word)
    def __search_recursive__(self, word, cur, index=0):
        if cur is None:
            return False
        if index == len(word):
            return cur.endOfWord
        ch = word[index]
        child = cur.children.get(ch, None)
        return self.__search_recursive__(word, child, index=index+1)

    def search_recursive(self, word):
        return self.__search_recursive__(word, self.__root__)


############################### DELETE ###############################


    # Time complexity: O(length_of_word)
    def __delete__(self, word, cur, index=0):
        if index == len(word):
            if cur.endOfWord:
                cur.endOfWord = False           # Mark `endOfWord` as we're going to delete this.
                return len(cur.children) == 0   # If there are no children, delete this node (True means node will be deleted later)
            return False

        ch = word[index]
        child = cur.children.get(ch, None)
        if child is None:
            return False                        # word doesn't exist.

        shouldRemove = self.__delete__(word, child, index=index+1)

        # Removing node from memory (i.e. parent's `children' dict) if this is the only node remaining in `children1 dict.
        if shouldRemove:
            # Delete this node from memory, i.e. remove node corresponding to key(ch) from it's parent's `children` dict
            cur.children.pop(ch)

            # If parent's `children` dict becomes empty then parent is also a candidate for removal, return `True` in that case.
            return len(cur.children) == 0
        return False

    def delete(self, word):
        self.__delete__(word, self.__root__)


############################### AUTO-COMPLETE (PREFIX SEARCH) ###############################


    def __prefix_search_joint_node__(self, prefix):
        cur = self.__root__
        for ch in prefix:
            child = cur.children.get(ch, None)
            if child is None:
                return None
            cur = child
        # If we reach here, it means there is at least 1 word starting with `prefix`
        return cur

    def __prefix_search__(self, prefix, joint_node):
        for ch, child_node in joint_node.children.items():
            prefix = prefix + ch
            if child_node.endOfWord:
                print prefix
            self.__prefix_search__(prefix, child_node)
            prefix = prefix[:-1]  # Backtracking

    def prefix_search(self, prefix):
        joint_node = self.__prefix_search_joint_node__(prefix)
        if joint_node is None:
            return
        self.__prefix_search__(prefix, joint_node)


############################### UPDATE ###############################


    # TODO
    def update(self, old_word, new_word):
        pass

############################### PRINT ###############################

    # TODO
    def print_trie(self):
        pass


def test():
    words = ["car", "card", "cards", "cardio", "carom", "carrot", "trie", "tries", "tried", "trial",
             "tree", "treat", "trio", "abcd", "pqrs", "abef", "abpr", "pqoj"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    print "'pars' is present? -", trie.search("pqrs")
    print "'abef' is present? -", trie.search_recursive("abef")

    print "\nDeleting 'pqrs'\n"
    trie.delete("pqrs")

    print "'pqrs' is present? -", trie.search("pqrs")
    print "'pqoj' is present? -", trie.search("pqoj")

    print '\n######################## AUTO-COMPLETE (PREFIX-SEARCH) #########################\n'

    search_prefixes = ["ca", "tr", "tri", "tre"]
    for pr in search_prefixes:
        print "\nWord(s) starting from '{}' are - ".format(pr)
        trie.prefix_search(pr)


# if __name__ == '__main__':
#     test()


if __name__ == '__main__':
    trie = Trie()
    choices = {
        1: "Insert",
        2: "Search",
        3: "Prefix search",
        4: "Delete",
        5: "Exit"
    }
    choices = '\n'.join(['{}. {}'.format(k,v) for k,v in choices.items()])

    while True:
        print "\n" + choices + "\n"
        try:
            choice = input("Enter your choice - ") or 0
        except:
            choice = 0

        if choice == 1:
            word = raw_input("Please enter a word/sequence to be inserted - ")
            trie.insert_recursive(word)
        elif choice == 2:
            word = raw_input("Please enter a word/sequence to be searched - ")
            is_present = trie.search(word)
            print "{} is {}present".format(word, "" if is_present else "not ")
        elif choice == 3:
            prefix = raw_input("Please enter a prefix of word/sequence to be searched - ")
            print "Word(s) starting from '{}' are -".format(prefix)
            trie.prefix_search(prefix)
        elif choice == 4:
            word = raw_input("Please enter a word/sequence to be deleted - ")
            trie.delete(word)
        elif choice == 5:
            print "Thank you!"
            break
        else:
            print "Invalid choice"
            continue